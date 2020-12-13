import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
plt.style.use('ggplot')

data = pd.read_csv('../Raw Data/julytemps.txt', skiprows=[0,1,2,3,4], header=None, sep=' ')
data.columns = ['Day', 'High', 'Low']
data.set_index('Day', inplace=True)



def get_meanstd(data, sampleSize, numSamples):
    gtMean = data.mean()
    gtStd = data.std()
    maxMeanDiff = 0.0
    maxStdDiff = 0.0
    sampleMeans = []

    for _ in range(numSamples):
        tseries = data.sample(sampleSize)
        sampleMean = tseries.mean()
        sampleStd = tseries.std()
        sampleMeans.append(sampleMean)
        _tmeandiff = abs(gtMean-sampleMean)
        _tstddiff = abs(gtStd-sampleStd)
        if _tmeandiff>maxMeanDiff: maxMeanDiff = _tmeandiff
        if _tstddiff>maxStdDiff: maxStdDiff = _tstddiff

    return sampleMeans, maxMeanDiff, maxStdDiff

highMeans, highMeanDiff, highStdDiff = get_meanstd(data.High, 8, 1000)
lowMeans, lowMeanDiff, lowStdDiff = get_meanstd(data.Low, 8, 1000)

plt.errorbar(['High', 'Low'],[np.mean(highMeans), np.mean(lowMeans)],
             yerr=3*np.array([highStdDiff, lowStdDiff]),
             fmt='.g', capsize=10, label='99.7% Confidence Interval')
plt.errorbar(['High', 'Low'],[np.mean(highMeans), np.mean(lowMeans)],
             yerr=1.96*np.array([highStdDiff, lowStdDiff]),
             fmt='.k', capsize=10, label='95% Confidence Interval')
plt.errorbar(['High', 'Low'],[np.mean(highMeans), np.mean(lowMeans)],
             yerr=1*np.array([highStdDiff, lowStdDiff]),
             fmt='.r', capsize=10, label='68% Confidence Interval')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.legend()
plt.show()

