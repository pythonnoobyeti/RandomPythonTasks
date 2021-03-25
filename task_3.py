data = {'lesson': [1594692000, 1594695600],
        'pupil': [1594692033, 1594696347],
        'tutor': [1594692017, 1594692066, 1594692068, 1594696341]}


def getVisitorsTime(timeDict):
    "Return student's and tutor's total time"
    studentTime = getTotalTime(timeDict['pupil'])
    tutorTime = getTotalTime(timeDict['tutor'])
    return studentTime, tutorTime  

def getTotalTime(timeList):
    "Return total time"
    sessionsAmount = getAmountSession(timeList)
    totalTime = 0
    for session in range(0, sessionsAmount):
        totalTime += timeList[1+session*2] - timeList[session*2]
    return totalTime

def getAmountSession(timeList):
    "Count visit sessions"
    return int(len(timeList)/2)

if __name__ == "__main__":
    studentTime, tutorTime = getVisitorsTime(data)
    print('====================================')
    print (f"Student's total time: {studentTime} s")
    print (f"Tutor's total time: {tutorTime} s")
    print('====================================')