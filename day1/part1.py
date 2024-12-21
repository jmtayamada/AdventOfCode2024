import pandas as pd

data = pd.read_csv('puzzleInput.csv', sep='   ', engine='python')

column1 = data.iloc[:, 0]
column2 = data.iloc[:, 1]

column1 = column1.sort_values()
column2 = column2.sort_values()

distance = 0
for x, y in zip(column1, column2):
    distance += abs(x - y)
    
print(distance)
