# Final Exam
### Problem 3


### You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket. Assume that once you draw a ball out of the bucket, you don't replace it. You draw 3 balls.

### Write a Monte Carlo simulation that meets the specifications below. Feel free to write a helper function if you wish.

```py
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
```

### Paste your entire function (including the definition) in the box.

### Restrictions:

- Do not import or use functions or methods from pylab, numpy, or matplotlib.
- Do not leave any debugging print statements when you paste your code in the box.

```py
import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
    three_same = 0.0
    for _ in range(numTrials):
        balls = [0,0,0,0,1,1,1,1] # 0-Red, Green-1
        ballpicks = 0
        for _ in range(3):
            picked_ball = random.choice(balls)
            balls.remove(picked_ball)
            ballpicks += picked_ball

        if int(ballpicks)==0 or  int(ballpicks)==3:
            three_same+=1
    prob = three_same/numTrials
    return prob
```
