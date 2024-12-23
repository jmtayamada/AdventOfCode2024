from numpy import fromstring, ndarray, delete
from math import copysign

data_file = "puzzleInput.csv"

dataList: list[ndarray] = []

# read data
with open(data_file, 'r') as temp_f:
    lines = temp_f.readlines()

    for l in lines:
        dataList.append(fromstring(l, dtype=int, sep=' '))


num_passed = len(dataList)


def CheckList(list: ndarray) -> bool:
    print(list)
    direction = None
    previousNumber = None
    for x in list:
        if previousNumber != None:
            difference = x - previousNumber
            if abs(difference) > 3:
                return False
            elif abs(difference) < 1:
                return False
            if direction != None:
                if direction != copysign(1, difference):
                    return False
            direction = copysign(1, difference)
        previousNumber = x
    return True


for list in dataList:
    if not CheckList(list):
        checks = False
        for i in range(len(list)):
            if CheckList(delete(list, i)):
                checks = True
        if checks == False:
            num_passed -= 1


print(num_passed)
