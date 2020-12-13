import random
# random.seed(0)
from tqdm import tqdm

def rollDie():
    return random.choice([1,2,3,4,5,6])


def runSim(goal, numTrials):
    total = 0
    for _ in tqdm(range(numTrials)):
        res = ''
        for _ in range(len(goal)):
            res += str(rollDie())
        if res == goal:
            total += 1
    print(f'Actual Probability of getting {goal} in {len(goal)} rolls of dice is : ', round(1/(6**len(goal)), 8))
    print(f'Emperical Probability of getting {goal} in {len(goal)} rolls of dice is : ', round(total/numTrials, 8))

runSim('11111', 1_000_000)



def boxCarsSim(numTrials):
    total=0
    for _ in range(numTrials):
        if rollDie()==6 & rollDie()==6:
            total += 1
    print(f'Actual Probability of getting {6,6} in {2} rolls of dice is : ', round(1/(6**2), 4))
    print(f'Emperical Probability of getting {6,6} in {2} rolls of dice is : ', round(total/numTrials, 4))

boxCarsSim(1_00_000)
