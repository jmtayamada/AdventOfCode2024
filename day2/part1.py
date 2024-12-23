from numpy import fromstring, ndarray
from math import copysign

data_file = "puzzleInput.csv"

dataList = []

# read data
with open(data_file, 'r') as temp_f:
    lines = temp_f.readlines()

    for l in lines:
        dataList.append(fromstring(l, dtype=int, sep=' '))


num_passed = len(dataList)


def CheckList(list: ndarray):
    global num_passed   # find better way to do this that doesn't require global
    direction = None
    previousNumber = None
    for x in list:
        if previousNumber != None:
            difference = x - previousNumber
            if abs(difference) > 3:
                num_passed -= 1
                print(str(list) + " failed, too large difference")
                break        # fail
            elif abs(difference) < 1:
                num_passed -= 1
                print(str(list) + " failed, too small difference")
                break
            if direction != None:
                if direction != copysign(1, difference):
                    num_passed -= 1
                    print(str(list) + " failed, wrong direction")
                    break    # fail
            direction = copysign(1, difference)
        previousNumber = x


for list in dataList:
    CheckList(list)


print(num_passed)
