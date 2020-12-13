import math
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

# FAIR ROULETTE
class FairRoulette:
    def __init__(self):
        self.pockets = list(range(1,37))
        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0
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


def playRoulette(game, numSpins, luckyNumber='9', toPrint=True):

    game = game()
    if toPrint : print(f'Running {game} for {numSpins:,} :')
    pocketWin = 0.0
    for _ in range(numSpins):
        game.spin()
        pocketWin += game.betPocket(luckyNumber,1)
    if toPrint:
        print(f'Expected return by betting on the Pocket={luckyNumber} : {100*pocketWin/numSpins:,} %')
        
    return pocketWin/numSpins

resultDict = {}
numTrials = 20
for G in (FairRoulette, AmericanRoulette, EuropeanRoulette):
    print('Playing : ', G())
    for numSpins in (100, 1000, 10_000, 100_000):
        kname = G().__str__()+'_'+str(numSpins)
        temp = []
        for etrial in range(numTrials):
            trialRet = playRoulette(G, numSpins, toPrint=False)
            temp.append(trialRet)
        resultDict[kname] = temp
        print(f'\tSimulating for {numSpins} of the game : ', np.mean(temp)*100, '+/-', np.std(temp)*100*1.96, ' for 95% Confidence Interval')

# resDF = pd.DataFrame(resultDict)
# resDF.plot()
# plt.show()
