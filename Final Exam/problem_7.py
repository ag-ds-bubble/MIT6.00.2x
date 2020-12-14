import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_data = [[25,1,4,10,1], # Person 1
            [19,1,10,30,1], # Person 2
            [26,1,5,90,1], # Person 3
            [57,1,1,100,0], # Person 4
            [60,1,1,120,0], # Person 5
            [40,1,6,60,0], # Person 6
            ]

df = pd.DataFrame(raw_data,
                  columns = ['Age', 'ContVis', 'Distance_NP', 'Income', 'Happy_Unhappy'],
                  index = ['Person1', 'Person2', 'Person3', 'Person4', 'Person5', 'Person6'])

featDf= df[['Distance_NP', 'Income']].copy()

manhattan_dist = lambda row1, row2 : sum(abs(row1-row2))

mDist = featDf.apply(lambda row1: featDf.apply(lambda row2 : manhattan_dist(row1, row2), axis=1), axis=1)
print('Manhattan Distance')
print(mDist)
import seaborn as sns
sns.heatmap(mDist, annot=True)
plt.show()