import random

def pickBall(availableBalls):
    choice = random.choice(availableBalls)
    availableBalls.remove(choice)
    return choice

def noReplacementSimulation(numTrials):
    three_sonsecutive_counts = 0.0
    for _ in range(numTrials):
        # Initialise
        available_balls = [0,0,0,1,1,1]
        picked = 0.0
        # Balls need to be drawn 3 times without replacement
        for epick in range(3):
            picked += pickBall(availableBalls=available_balls)
        if picked==0.0 or picked==3.0:
            three_sonsecutive_counts+=1
    return three_sonsecutive_counts/numTrials