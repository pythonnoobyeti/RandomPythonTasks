def getFirstIndex(stringOfNumbers):
    "Return the first index of 0 in stringOfNumbers"
    return stringOfNumbers.index("0")


if __name__ == "__main__":
    stringOfNumbers = "111111111111111111111111100000000"
    print(f"The first index of 0 is {getFirstIndex(stringOfNumbers)}.")