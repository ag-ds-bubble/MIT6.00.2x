import random
random.seed(0)


numCasesPerYear = 36_000
numYears = 3
stateSize = 10_000
communitySize = 10
numCommunities = stateSize//communitySize
numTrials = 100
numGreater = 0

for _ in range(numTrials):
    locs = [0]*numCommunities
    for _ in range(numYears*numCasesPerYear):
        locs[random.choice(range(numCommunities))] += 1
    if max(locs)>=143:
        numGreater+=1

prob = round(numGreater/numTrials, 3)
print('Est Probability of at least one region crossing 143 mark is ', prob)


