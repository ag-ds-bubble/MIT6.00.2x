## Finger Exercise 4

### You have a bucket with 3 red balls and 3 green balls. Assume that once you draw a ball out of the bucket, you don't replace it. What is the probability of drawing 3 balls of the same color?

### Write a Monte Carlo simulation to solve the above problem. Feel free to write a helper function if you wish.

```py
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
```