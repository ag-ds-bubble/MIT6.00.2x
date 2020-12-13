import random
import numpy as np

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'<{self.x}, {self.y}>'
    def move(self, deltaX, deltaY):
        return Location(self.x+deltaX, self.y+deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getPos(self):
        return (self.x, self.y)
    def distFrom(self, other):
        return ((self.x-other.getX())**2 + (self.y-other.getY())**2)**0.5

class Field(object):
    def __init__(self):
        self.drunks = {}
    def addDrunk(self, drunk, loc=None):
        if not loc:
            loc = Location(0,0)
        if drunk in self.drunks:
            raise ValueError(f"{drunk} already in the field")
        else:
            self.drunks[drunk]=loc
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        return self.drunks[drunk]
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in the field!")
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

class OddField(Field):
    def __init__(self, numHoles=1000, xRange=100, yRange=100):
        Field.__init__(self)
        self.wormHoles = {}
        for _ in range(numHoles):
            x = random.randint(-xRange, xRange)
            newx = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newy = random.randint(-yRange, yRange)
            newLoc = Location(newx, newy)
            self.wormHoles[(x,y)] = newLoc
    def moveDrunk(self, drunk):
        Field.moveDrunk(self, drunk)
        pos = self.drunks[drunk].getPos()
        if pos in self.wormHoles:
            self.drunks[drunk] = self.wormHoles[pos]

class Drunk:
    def __init__(self, name):
        self.name=name
    def __str__(self):
        return f'This drunk is named : {self.name}'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    """Want to move more south in relative to north.."""
    def takeStep(self):
        stepChoices = [(0.0,0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    Homer = dClass('Drunk')
    origin = Location(0,0)
    distances = []
    for _ in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances


def getFinalLoc(numSteps, numTrials, dClass):
    Homer = dClass('Drunk')
    origin = Location(0,0)
    finalLocs = []
    for _ in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        _=walk(f, Homer, numSteps)
        finalLocs.append(f.getLoc(Homer).getPos())
    return finalLocs

def testDrunk(diffSteps):
    for drunkType in [UsualDrunk, ColdDrunk]:
        print(f'\n\nSimulating {drunkType.__name__}')
        for nt in [100]:
            for nst in diffSteps:
                simDist=[]
                print(f'\t For NumTrials : {nt}, NumSteps : {nst}')
                simDist = simWalks(nst, nt, drunkType)
                print('\t\tMean', round(np.mean(simDist), 3))
                print('\t\tMax', round(np.max(simDist), 3), '; Min', round(np.min(simDist), 3))


if __name__ == '__main__':
    random.seed(0)
    testDrunk([10, 100, 1000, 10_000])

