# Imports
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Load the data
data = pd.read_csv('../Raw Data/temperatures.csv', parse_dates=True)
data.DATE = pd.to_datetime(data.DATE,format='%Y%m%d')
data.set_index('DATE', inplace=True)
population = data.TEMP.values.tolist()




# Testing for the independence
random.seed(0)
popMean = np.mean(population)
popStd = np.std(population)
sampleSize = 200
numTrials = 10_000
numBad = 0

for _ in range(numTrials):
    sample = random.sample(population, sampleSize)
    sampleMean = np.mean(sample)
    sampleMeanSE = np.std(sample)/np.sqrt(sampleSize)

    if abs(popMean-sampleMean)>1.96*sampleMeanSE:
        numBad+=1
print(f'% Outside 95% interval @ i.i.d : {round(100*numBad/numTrials,3)} %')




# Testing for the independence
random.seed(0)
popMean = np.mean(population)
popStd = np.std(population)
sampleSize = 200
numTrials = 10_000
numBad = 0

for _ in range(numTrials):
    spts = range(0, len(population)-sampleSize)
    start = random.choice(spts)
    sample = population[start:start+sampleSize]
    sampleMean = np.mean(sample)
    sampleMeanSE = np.std(sample)/np.sqrt(sampleSize)

    if abs(popMean-sampleMean)>1.96*sampleMeanSE:
        numBad+=1
print(f'% Outside 95% interval not @ i.i.d : {round(100*numBad/numTrials,3)} %')

