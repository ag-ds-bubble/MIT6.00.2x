import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
plt.style.use('ggplot')

data = pd.read_csv('../Raw Data/temperatures.csv', parse_dates=True)
data.DATE = pd.to_datetime(data.DATE,format='%Y%m%d')
data.set_index('DATE', inplace=True)

def get_meanstd(data, sampleSize, numSamples):
    gtMean = data.TEMP.mean()
    gtStd = data.TEMP.std()
    maxMeanDiff = 0.0
    maxStdDiff = 0.0
    sampleMeans = []

    for _ in range(numSamples):
        tdf = data.sample(sampleSize)
        sampleMean = tdf.TEMP.mean()
        sampleStd = tdf.TEMP.std()
        sampleMeans.append(sampleMean)
        _tmeandiff = abs(gtMean-sampleMean)
        _tstddiff = abs(gtStd-sampleStd)
        if _tmeandiff>maxMeanDiff: maxMeanDiff = _tmeandiff
        if _tstddiff>maxStdDiff: maxStdDiff = _tstddiff

    return sampleMeans, maxMeanDiff, maxStdDiff


def sample_mean_analysis(data, sampleSize, numSamples=1000, toPrint=False):

    sampleMeans, maxMeanDiff, maxStdDiff = get_meanstd(data, sampleSize, numSamples)
    if toPrint:
        print(f'\nMean of the Sample Means for sample size = {sampleSize} : {round(np.mean(sampleMeans), 3)}')
        print(f'Std of the Sample Means for sample size = {sampleSize}  : {round(np.std(sampleMeans), 3)}')
        print(f'Max Diff in Sample Means for sample size = {sampleSize}  : {round(maxMeanDiff, 3)}')
        print(f'Max Diff in Sample Std for sample size = {sampleSize}  : {round(maxStdDiff, 3)}')

    return np.mean(sampleMeans), maxMeanDiff, maxStdDiff

def plot_errorBars(data, sampleS):
    _smeans = []
    _smdiff = []
    _sddiff = []
    for essize in tqdm(sampleS):
        _ms, _mmd, _msd = sample_mean_analysis(data, sampleSize=essize, numSamples=100)
        _smeans.append(_ms)
        _smdiff.append(_mmd)
        _sddiff.append(_msd)

    plt.errorbar(sampleS, _smeans, yerr=1.96*np.array(_sddiff), fmt='.k', capsize=10, label='95% Confidence Interval')
    plt.axhline(data.TEMP.mean(), 0, max(sampleS), color='r', label='Mean of the samples')
    plt.xlabel('Temperature')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()


# sample_mean_analysis(data, 200)
plot_errorBars(data, [100,200,300,400,500,1000,1500,2000])
