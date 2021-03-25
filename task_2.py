from bs4 import BeautifulSoup
import requests
import json


def printLoading():
    "Print loading string"
    point = '.'
    if loadingCounter == 10:
        print('          ', end='\r')
    else:
        print(f'{point*loadingCounter}', end='\r', flush=True)


animalsLibrary = {}
rootURL = 'https://ru.wikipedia.org'
pageURL = """/w/index.php?title=Категория:Животные_по_алфавиту&from=А"""
russianLetter = True  # check russian letter
loadingCounter = 0


if __name__ == "__main__":
    while russianLetter:
        if loadingCounter > 10:
            loadingCounter = 0  # reset loading counter
        printLoading()
        source = requests.get(rootURL + pageURL).text
        soup = BeautifulSoup(source, 'lxml')
        # get all divs that contain elements with animals name
        animalSet = soup.find_all('div', class_='mw-category-group')

        # process all divs
        for animals in animalSet:
            letter = animals.h3.text  # get current letter in div
            # if english letter - break
            if (letter == 'A'):
                russianLetter = False
                break
            # get elements with animal names
            animalsName = animals.ul.find_all('a')

            if (letter not in animalsLibrary.keys()):
                animalsLibrary[letter] = []

            for name in animalsName:
                animalsLibrary[letter].append(name.text)

        try:
            pageURL = soup.find('a', text='Следующая страница')['href']
        except Exception:
            break
        loadingCounter += 1


    filename = 'animals.json'
    with open(filename, 'w', encoding="utf-8") as f_obj:
        json.dump(animalsLibrary, f_obj, indent=2, ensure_ascii=False)

    for key, value in animalsLibrary.items():
        print(f'{key}: {len(value)}')
