import random
import numpy as np

def throwDots(numDots):
    inSine=0
    for _ in range(numDots):
        x = random.uniform(0,np.pi)
        y = random.uniform(0,1)
        if y<=np.sin(x):
            inSine += 1
    return np.pi*(inSine/float(numDots))


def getEst(numDots, numTrials):
    estimates = []
    for _ in range(numTrials):
        sinGuess = throwDots(numDots)
        estimates.append(sinGuess)
    currEst = round(np.mean(estimates),10)
    currStd = round(np.std(estimates),10)
    print(f'For {numDots} > Est : {currEst}; Std : {currStd}')
    return currEst, currStd


def estSin(precision, numTrials):
    numDots = 1000
    sDev = precision
    while sDev >= precision/1.96:
        currEst, sDev = getEst(numDots, numTrials)
        numDots *= 2
    return currEst

estSin(0.005, 100)