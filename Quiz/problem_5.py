import math
import numpy as np
import matplotlib.pyplot as plt

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getCoordinates(self):
        return self.x, self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


import random

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name


# New code
# The following function is new, and returns the actual x and y distance from the start point to the end point of a random walk.

def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())
 

# drunk variations
# Here are several different variations on a drunk.

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)] 
        return random.choice(stepChoices)

# Initialisations
field = Field()
udrunk = UsualDrunk('Usual Drunk') 
cdrunk = ColdDrunk('Cold Drunk')
edrunk = EDrunk('E Drunk')
pdrunk = PhotoDrunk('Photo Drunk')
ddrunk = DDrunk('D Drunk')

field.addDrunk(udrunk, Location(0,0))
field.addDrunk(cdrunk, Location(0,0))
field.addDrunk(edrunk, Location(0,0))
field.addDrunk(pdrunk, Location(0,0))
field.addDrunk(ddrunk, Location(0,0))

udrunk_loc_x = []
udrunk_loc_y = []

cdrunk_loc_x = []
cdrunk_loc_y = []

edrunk_loc_x = []
edrunk_loc_y = []

pdrunk_loc_x = []
pdrunk_loc_y = []

ddrunk_loc_x = []
ddrunk_loc_y = []


for _ in range(10_000):
    udrunk_loc_x.append(field.getLoc(udrunk).getX())
    udrunk_loc_y.append(field.getLoc(udrunk).getY())
    field.moveDrunk(udrunk)
    
    cdrunk_loc_x.append(field.getLoc(cdrunk).getX())
    cdrunk_loc_y.append(field.getLoc(cdrunk).getY())
    field.moveDrunk(cdrunk)
    
    edrunk_loc_x.append(field.getLoc(edrunk).getX())
    edrunk_loc_y.append(field.getLoc(edrunk).getY())
    field.moveDrunk(edrunk)
    
    pdrunk_loc_x.append(field.getLoc(pdrunk).getX())
    pdrunk_loc_y.append(field.getLoc(pdrunk).getY())
    field.moveDrunk(pdrunk)
    
    ddrunk_loc_x.append(field.getLoc(ddrunk).getX())
    ddrunk_loc_y.append(field.getLoc(ddrunk).getY())
    field.moveDrunk(ddrunk)


    
udrunk_locs = np.c_[udrunk_loc_x, udrunk_loc_y]
cdrunk_locs = np.c_[cdrunk_loc_x, cdrunk_loc_y]
edrunk_locs = np.c_[edrunk_loc_x, edrunk_loc_y]
pdrunk_locs = np.c_[pdrunk_loc_x, pdrunk_loc_y]
ddrunk_locs = np.c_[ddrunk_loc_x, ddrunk_loc_y]
    
for edtype, ename in zip([udrunk_locs, cdrunk_locs, edrunk_locs, pdrunk_locs, ddrunk_locs],
               ['Usual Drunk', 'Cold Drunk', 'E Drunk', 'P Drunk', 'D Drunk']):
    
    plt.figure()
    plt.scatter(edtype[:,0], edtype[:,1], s=1, color='r')
    plt.xlim(-100,100)
    plt.ylim(-100,100)
    plt.title(ename)
    plt.grid()

plt.show()