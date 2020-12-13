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

def checkSEM(data):
    # Testing Standard Error of the Mean
    sampleSizes = (25, 50, 100, 200, 300, 400, 500, 600)
    numTrials = 50
    population = data.TEMP.values.tolist()
    popSD = np.std(population)
    sems = []
    sampleSDs = []

    for size in sampleSizes:
        _se = popSD/np.sqrt(size)
        sems.append(_se)
        means = []
        for _ in range(numTrials):
            sample = random.sample(population, size)
            means.append(np.mean(sample))
        sampleSDs.append(np.std(means))

    plt.plot(sampleSizes, sems, '-r', label='Standard Error of the Mean')
    plt.plot(sampleSizes, sampleSDs, ':k', label='Standard Deviation')
    plt.title('SEM vs SD for 50 means')
    plt.legend()
    plt.show()



def sampleSDvcPSD(population, legend='STD of Temperatures', cicolor = 'darkgray'):
    popSD = np.std(population)
    numTrials = 50
    maxSampleSize = 600
    samples =  range(10, maxSampleSize, 10)
    std_mean = []
    std_95err = []
    for ssize in samples:
        sampleSDdeviat = []
        for _ in range(numTrials):
            sstd = np.std(random.sample(population, ssize))
            sdeviat = abs(popSD-sstd)/popSD
            sampleSDdeviat.append(sdeviat*100)
        std_mean.append(np.mean(sampleSDdeviat))
        std_95err.append(1.96*np.std(sampleSDdeviat))
    samples = np.array(samples)
    std_mean = np.array(std_mean)
    std_95err = np.array(std_95err)
    plt.plot(samples, std_mean, '.', color=cicolor, label=legend)
    plt.fill_between(samples,
                     std_mean-1.96*std_95err,
                     std_mean+1.96*std_95err, interpolate=True, color=cicolor,
                     label='95% Confidence Interval of STD of Sample', alpha=0.4)
    plt.axhline(min(std_mean), 0, maxSampleSize, linestyle=':', color='r')
    print('Minimum STD : ', round(min(std_mean), 3), '%')
    


# checkSEM(data)

# sampleSDvcPSD(data.TEMP.values.tolist())
# plt.xlabel('Sample Size')
# plt.ylabel('% Diff from Population SD')
# plt.title('% Deviations ')
# plt.legend()
# plt.show()


def testDistributions():
    uniform, normal, exp = [], [], []
    for _ in range(100_000):
        uniform.append(random.uniform(0,1))
        normal.append(random.gauss(0,1))
        exp.append(random.expovariate(0.5))
    # plt.hist(uniform, label='Uniform Distribution')
    # plt.figure()
    # plt.hist(normal, label='Normal Distribution')
    # plt.figure()
    # plt.hist(exp, label='Exponential Distribution')
    # plt.legend()
    # plt.show()

    # STD based on Distribution
    sampleSDvcPSD(uniform, legend='Uniform Distribution', cicolor='darkgray')
    sampleSDvcPSD(normal, legend='Normal Distribution', cicolor='lightgreen')
    sampleSDvcPSD(exp, legend='Exponential Distribution', cicolor='red')
    plt.xlabel('Sample Size')
    plt.ylabel('% Diff from Population SD')
    plt.title('% Deviations ')
    plt.legend()
    plt.show()

testDistributions()


def testPopulationSize():
    population1 = [random.uniform(0,1) for _ in range(100_000)]
    population2 = [random.uniform(0,1) for _ in range(1_000_000)]
    population3 = [random.uniform(0,1) for _ in range(10_000_000)]

    # STD based on population size
    sampleSDvcPSD(population1, legend='100_000', cicolor='darkgray')
    sampleSDvcPSD(population2, legend='1_000_000', cicolor='lightgreen')
    sampleSDvcPSD(population3, legend='10_000_000', cicolor='red')
    plt.xlabel('Sample Size')
    plt.ylabel('% Diff from Population SD')
    plt.title('% Deviations ')
    plt.legend()
    plt.show()


# testPopulationSize()
