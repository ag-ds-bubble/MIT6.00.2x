import math
import random

# Probability of a coin
def coin_prob(n, heads):
    probability = math.comb(n,heads)/(2**n)
    print(f'Probability of getting {heads} Heads from n={n} trials is : {probability}')

def test_coin_prob():
    print('\n\n##################### COIN PROBABILITY ###################')
    coin_prob(1,1)
    coin_prob(2,2)
    coin_prob(100,100)
    coin_prob(100,52)
    print('\n\n\n')

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

    def isBlack(self):
        if self.ball:
            if (self.ball>0 and self.ball<=10) or (self.ball>18 and self.ball<=28):
                return self.ball%2==0
            else:
                return self.ball%2==1
        else:
            return False

    def isRed(self):
        if self.ball:
            return not self.isBlack()
        else:
            return False

    def betBlack(self, amt):
        if self.isBlack():
            return amt*self.blackOdds
        else:
            return -amt

    def betRed(self, amt):
        if self.isRed():
            return amt*self.redOdds
        else:
            return -amt
            
    def betPocket(self, pocket, amt):
        if str(pocket)==str(self.ball):
            return amt*self.pocketOdds
        else:
            return -amt


def playRoulette(game, numSpins, luckyNumber='9', toPrint=True):

    game = game()
    if toPrint : print(f'Running {game} for {numSpins:,} :')
    redWin, blackWin, pocketWin = 0.0, 0.0, 0.0
    for _ in range(numSpins):
        game.spin()
        redWin += game.betRed(1)
        blackWin += game.betBlack(1)
        pocketWin += game.betPocket(luckyNumber,1)
    if toPrint:
        print(f'Expected return by betting on the Red Color : {100*redWin/numSpins:,} %')
        print(f'Expected return by betting on the Black Color : {100*blackWin/numSpins:,} %')
        print(f'Expected return by betting on the Pocket={luckyNumber} : {100*pocketWin/numSpins:,} %')
        
    
# Coin Probability
test_coin_prob()

# Fair Roulette Simulation
playRoulette(FairRoulette, numSpins=1_000_000)

