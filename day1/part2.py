import pandas as pd

data = pd.read_csv('puzzleInput.csv', sep='   ', engine='python')

column1 = data.iloc[:, 0]
column2 = data.iloc[:, 1]

column2 = column2.to_list()

similarity_score = 0

for x in column1:
    similarity_score += x * column2.count(x)

print(similarity_score)