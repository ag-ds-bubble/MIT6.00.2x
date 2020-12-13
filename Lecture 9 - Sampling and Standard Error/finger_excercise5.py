# Imports
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Load the data
population1 = pd.read_csv('../Raw Data/hr1.txt', sep='\n', header=None)
population2 = pd.read_csv('../Raw Data/hr2.txt', sep='\n', header=None)

# Looking at the time series
# population1.plot()
# plt.figure()
# population2.plot()
# plt.show()



# Testing for various Sampling Techniques
for population, popname in zip([population1.iloc[:,0].values.tolist(), population2.iloc[:,0].values.tolist()], ['Pop1', 'Pop2']):
    print('\nAnalysing for ', popname)
    random.seed(0)
    popMean = np.mean(population)
    popStd = np.std(population)
    sampleSize = 250
    numTrials = 10_000
    numBad = 0

    for _ in range(numTrials):
        sample = random.sample(population, sampleSize)
        sampleMean = np.mean(sample)
        sampleMeanSE = np.std(sample)/np.sqrt(sampleSize)

        if abs(popMean-sampleMean)>1.96*sampleMeanSE:
            numBad+=1
    print(f'\t% Outside 95% interval @ random.sample : {round(100*numBad/numTrials,3)} %')

    numBad = 0
    for _ in range(numTrials):
        sample = [population[random.randint(0,1800-1)] for _ in range(sampleSize)]
        sampleMean = np.mean(sample)
        sampleMeanSE = np.std(sample)/np.sqrt(sampleSize)

        if abs(popMean-sampleMean)>1.96*sampleMeanSE:
            numBad+=1
    print(f'\t% Outside 95% interval @ [0,1800] : {round(100*numBad/numTrials,3)} %')
