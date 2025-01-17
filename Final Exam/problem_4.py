import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()    
                    
# Implement this -- Coding Part 2 of 2
from itertools import groupby
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    # """

    
    # longestRuns = []
    # for _ in range(numTrials):
    #     outcomes = []
    #     for _ in range(numRolls):
    #         outcomes.append(die.roll())
    #     # Figure out the longest run
    #     outcome_diffs = []
    #     for ii, iin in zip(outcomes[:-1], outcomes[1:]):
    #         outcome_diffs.append(iin-ii)
    #     count_dups = [sum(1 for _ in group) for _, group in groupby(outcome_diffs)]
    #     if count_dups!=[]:
    #         count_dups = max(count_dups)+1
    #     else:
    #         count_dups = 1
    #     # Update Longest Runs
    #     longestRuns.append(count_dups)

    # makeHistogram(longestRuns, numBins = 10, xLabel = 'Length of longest run', yLabel = 'frequency', title = 'Histogram of longest runs')
    longest_runs = []
    for i in range(numTrials):
        rolls = [die.roll() for j in range(numRolls)]
        size = 1
        max_size = 0
        for i in range(len(rolls)-1):
            if rolls[i+1] == rolls[i]:
                size += 1
            else: 
                size = 1
            if max_size < size:
                max_size = size
        if max_size > 0:
            longest_runs.append(max_size)
        else:
            longest_runs.append(1)
    makeHistogram(longest_runs, numBins = 10, xLabel = 'Length of longest run', yLabel = 'frequency', title = 'Histogram of longest runs')

    lrMean = sum(longest_runs)/numTrials
    return lrMean


# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 50, 1000))
print(getAverage(Die([1,2,3,4,5,6]), 50, 1000))
print(getAverage(Die([1,1]), 10, 1000))