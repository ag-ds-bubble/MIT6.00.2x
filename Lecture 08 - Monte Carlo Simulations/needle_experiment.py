import random
import numpy as np

def throwNeedles(numNeedles):
    inCircle=0
    for _ in range(numNeedles):
        x = random.random()
        y = random.random()
        if (x**2+y**2)**0.5<=1.0:
            inCircle += 1
    return 4*(inCircle/float(numNeedles))


def getEst(numNeedles, numTrials):
    estimates = []
    for _ in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    currEst = round(np.mean(estimates),10)
    currStd = round(np.std(estimates),10)
    print(f'For {numNeedles} > Est : {currEst}; Std : {currStd}')
    return currEst, currStd


def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/1.96:
        currEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return currEst

estPi(0.005, 100)