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

actProb = 1/7
simProb = drawing_without_replacement_sim(10_00_000)

print(f'Difference from the actual : {round(100*((actProb-simProb)/actProb),3)}')

