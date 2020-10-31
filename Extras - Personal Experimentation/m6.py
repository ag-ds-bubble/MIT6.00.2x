"""
MONTE CARLO SIMULATIONS
"""
# Imports
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from matplotlib import animation

def playRoulette(game, pocket, betamt, numspins, to_print = True):
    totPocket = 0
    for _ in range(numspins):
        game.spin()
        totPocket += game.betPocket(pocket, betamt)
    if to_print:
        exret = np.round(100*(totPocket/numspins), 3)
        print(f'{numspins} spins of {game}, will have expected return of {exret} % ')

    return totPocket/numspins

# Fair Roulette
class FairRoulette:
    def __init__(self):
        self.pockets = [str(k) for k in list(range(1,37))]
        self.ball = None
        self.pocketOdds = len(self.pockets)-1

    def __str__(self):
        return "    Fair Roulette"

    def spin(self):
        # Spin the Wheel
        self.ball = np.random.choice(self.pockets)

    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else:
            return -amt

# European Roulette
class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    def __str__(self):
        return "European Roulette"

# American Roulette
class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')
    def __str__(self):
        return "American Roulette"

def runall_roulettes():
    gameF = FairRoulette()
    gameE = EuRoulette()
    gameA = AmRoulette()
    for _spins in [100, 1_000, 10_000, 100_000, 1_000_000]:
        for G in [gameF, gameE, gameA]:
            pnl=[]
            for i in range(20):
                pnl.append(playRoulette(G, 2, 1, numspins=_spins, to_print=False))

            _var = np.round(np.var(pnl)*100, 3)
            _mean = np.round(np.mean(pnl)*100, 3)
            _std = np.round(np.std(pnl)*100, 3)
            _ci = np.round(1.96*_std, 3)

            print(f'For game : {G} with {_spins} Spins, Expected return would be {_mean}, with Variance {_var} and Standard Deviation {_std} @ +/- {_ci}% Confidence Interval')
        print()

# runall_roulettes()



