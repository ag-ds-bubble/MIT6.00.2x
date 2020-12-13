# Imports
import pandas as pd
import numpy as np

raw_data = [[1,1,1,1,0,1], # Cobra
            [1,1,1,1,0,1], # Rattle snake
            [0,1,0,1,0,1], # Boa Constrictor
            [1,1,0,1,2,0], # Chicken
            [0,1,0,0,0,0], # Guppy
            [1,0,1,0,4,0], # Dart Frog
            [0,0,0,0,4,0], # Zebra
            [1,1,0,1,0,1], # Python
            [1,1,0,1,4,1], # Alligator
            ]

df = pd.DataFrame(raw_data,
                  columns = ['Egg-Laying', 'Scales', 'Poisounous', 'Cold-Blooded', 'Number Legs', 'Reptile'],
                  index = ['Cobra', 'Rattle Snake', 'Boa Constrictor', 'Chicken', 'Guppy', 'Dart Frog', 'Zebra', 'Python', 'Alligator'])

featDf= df.iloc[:, :-1].copy()

manhattan_dist = lambda row1, row2 : sum(abs(row1-row2))
euclidean_dist = lambda row1, row2 : round(np.sqrt(sum(abs(row1-row2)**2)), 2)

mDist = featDf.apply(lambda row1: featDf.apply(lambda row2 : manhattan_dist(row1, row2), axis=1), axis=1)
eDist = featDf.apply(lambda row1: featDf.apply(lambda row2 : euclidean_dist(row1, row2), axis=1), axis=1)

print('Manhattan Distance')
print(mDist)
print('\n\n\nEuclidean Distance')
print(eDist)

featDf = featDf/featDf.max()
eDist = featDf.apply(lambda row1: featDf.apply(lambda row2 : euclidean_dist(row1, row2), axis=1), axis=1)
print('\n\n\nScaled Euclidean Distance')
print(eDist)
