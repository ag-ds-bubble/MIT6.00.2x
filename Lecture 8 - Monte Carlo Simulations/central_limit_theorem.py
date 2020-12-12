import matplotlib.pyplot as plt
import random
import numpy as np

def plotrolls(numDice, numRolls, numBins, color, legend, style, toPrint=False):
    means = []
    for eroll in range(numRolls//numDice):
        mean_val = 0.0
        for edice in range(numDice):
            # mean_val += np.random.choice([1,2,3,4,5,6]) ## Actual Dice
            mean_val += 5*random.random() ## Fictitous Dice, with continous values from 0-5
        means.append(mean_val/float(numDice))
    plt.hist(means, numBins, color=color, label=legend, 
             weights=np.ones(len(means))/len(means), hatch=style)
    if toPrint:
        print(f'Mean for {legend} for {numRolls//numDice} rolls each sample is = {round(np.mean(means),3)}, with std of {round(np.std(means),3)}')
    
# plotrolls(numDice=1, numRolls=10_00_000, numBins=19, color='b', legend='1 Die', style='*', toPrint=True)
# plotrolls(numDice=50, numRolls=10_00_000, numBins=19, color='r', legend='50 Die', style='//', toPrint=True)
# plotrolls(numDice=500, numRolls=10_00_000, numBins=19, color='g', legend='500 Die', style='\\', toPrint=True)
# plt.legend()
# plt.show()



# FAIR ROULETTE
class FairRoulette:
    def __init__(self):
        self.pockets = list(range(1,37))
        self.ball = None
        self.pocketOdds = len(self.pockets) - 1.0

    def __str__(self):
        return "Fair Roulette"

    def spin(self):
        self.ball = random.choice(self.pockets)

    def betPocket(self, pocket, amt):
        if str(pocket)==str(self.ball):
            return amt*self.pocketOdds
        else:
            return -amt


class EuropeanRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    def __str__(self):
        return "European Roulette"


class AmericanRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
        self.pockets.append('00')
    def __str__(self):
        return "American Roulette"

def plotRoulette(gameC, numSpins, numTrials, numBins, color, legend, style, luckyNumber='9', toPrint=True):
    means = []
    for _ in range(numTrials//numSpins):
        game = gameC()
        pocketWin = 0.0
        for _ in range(numSpins):
            game.spin()
            pocketWin += game.betPocket(luckyNumber,1)
        means.append(pocketWin/numSpins)
    if toPrint:
        print(f'Expected return by betting on the Pocket={luckyNumber} for numTrials={numTrials}: {100*pocketWin/numSpins:,} %')

    plt.hist(means, numBins, color=color, label=legend, 
             weights=np.ones(len(means))/len(means), hatch=style, alpha=0.4)



numt = 1_000_000
plotRoulette(gameC=FairRoulette, numSpins=1000, numTrials=numt, numBins=19, color='b', legend='100_000 FR Spin', style='*', toPrint=True)
plotRoulette(gameC=EuropeanRoulette, numSpins=1000, numTrials=numt, numBins=19, color='r', legend='100_000 ER Spin', style='//', toPrint=True)
plotRoulette(gameC=AmericanRoulette, numSpins=1000, numTrials=numt, numBins=19, color='g', legend='100_000 AR Spin', style='\\', toPrint=True)
plt.legend()
plt.show()