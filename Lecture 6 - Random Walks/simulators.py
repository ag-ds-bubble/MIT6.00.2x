from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

from random_walk import walk, simWalks, testDrunk, UsualDrunk, ColdDrunk, getFinalLoc, random, Field, OddField

def styleIterator(styles):
    idx=-1
    while True:
        idx+=1
        yield styles[idx%len(styles)]

styleChoiceL = styleIterator(['m-', 'b--', 'g-.'])
styleChoiceS = styleIterator(['k+', 'r^', 'mo'])

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print(f'Starting Simulation for {dClass.__name__} {numSteps} steps')
        trial = simWalks(numSteps, numTrials, dClass)
        meanDistances.append(sum(trial)/len(trial))
    return meanDistances

# simMeanDist = simDrunk(100, UsualDrunk, [1, 10,100,1000,10_000])
# plt.plot([1,10,100,1000,10_000], simMeanDist, next(styleChoice), label=UsualDrunk.__name__)
# simMeanDist = simDrunk(100, ColdDrunk, [1, 10, 100,1000,10_000])
# plt.plot([1,10,100,1000,10_000], simMeanDist, next(styleChoice), label=ColdDrunk.__name__)
# plt.legend()
# plt.title('Mean Distance Convered')
# plt.show()


def plotLocs(drunkKinds, numSteps, numTrials):
    for dClass in drunkKinds:
        finalLocs = getFinalLoc(numSteps,numTrials,dClass)
        finalLocsX, finalLocsY = np.array(finalLocs)[:,0], np.array(finalLocs)[:,1]
        plt.plot(finalLocsX, finalLocsY, next(styleChoiceS), label=dClass.__name__+f'<{abs(round(np.mean(finalLocsX), 1))}, {abs(round(np.mean(finalLocsY), 1))}>')
    plt.xlim(-1000, 1000)
    plt.ylim(-1000, 1000)
    plt.title(f'Location at the End of {numTrials} Trials, after {numSteps} Steps')
    plt.legend()
    plt.show()

# random.seed(0)
# plotLocs([UsualDrunk, ColdDrunk], 10_000, 1000)


# Walk Simulator
class Simulator(object):
    def __init__(self, numSteps):
        self.numSteps = numSteps
        self.fig, self.axes = plt.subplots()
        # Initialise Fields & Drunks
        self.regField = Field()
        self.oddField = OddField()
        self.uDrunkR = UsualDrunk('Usual')
        self.cDrunkR = UsualDrunk('Cold')
        self.uDrunkO = UsualDrunk('Usual')
        self.cDrunkO = UsualDrunk('Cold')
        # Add drunks to the fields
        self.regField.addDrunk(self.uDrunkR)
        self.regField.addDrunk(self.cDrunkR)
        self.oddField.addDrunk(self.uDrunkO)
        self.oddField.addDrunk(self.cDrunkO)
        
    def getAllPos(self):
        positions = np.array([self.regField.getLoc(self.uDrunkR).getPos(),
                             self.regField.getLoc(self.cDrunkR).getPos(),
                             self.oddField.getLoc(self.uDrunkO).getPos(),
                             self.oddField.getLoc(self.cDrunkO).getPos()])
        return positions[:,0], positions[:,1]


    def init_plot(self):
        self.axes.set_title(f'Field v/s Odd Field @ {self.numSteps}')
        self.axes.set_xlabel('East/West Steps')
        self.axes.set_ylabel('North/South Steps')
        allX, allY = self.getAllPos()
        self.pos_graph = self.axes.scatter(allX, allY, color=['k','r','k','r'], s=4)
        self.pos_annots = [self.axes.text(_x,_y,_name) for _x,_y,_name in zip(allX, allY, [UsualDrunk.__name__, ColdDrunk.__name__]*2)] 
        self.axes.grid('both')
        self.axes.set_ylim(-1000, 1000)
        self.axes.set_xlim(-1000, 1000)
        return self.pos_graph,self.pos_annots

    def update_plot(self, i):
        # Move each of the drunks
        # get the new vals 
        # Update the plot
        self.regField.moveDrunk(self.uDrunkR)
        self.regField.moveDrunk(self.cDrunkR)
        self.oddField.moveDrunk(self.cDrunkO)
        self.oddField.moveDrunk(self.uDrunkO)

        allX, allY = self.getAllPos()
        self.pos_graph.set_offsets(np.c_[allX, allY])

        self.pos_annots[0].set_position((allX[0], allY[0]))
        self.pos_annots[1].set_position((allX[1], allY[1]))
        self.pos_annots[2].set_position((allX[2], allY[2]))
        self.pos_annots[3].set_position((allX[3], allY[3]))
        return self.pos_graph,self.pos_annots

    def runSimulation(self):
        self.ani = FuncAnimation(self.fig, self.update_plot, frames=self.numSteps,
                                 init_func=self.init_plot, blit=False)
        plt.show()


movementSim = Simulator(10_000)
movementSim.runSimulation()