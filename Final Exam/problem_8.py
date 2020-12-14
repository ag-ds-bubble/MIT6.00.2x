import random
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# import os
# os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
np.random.seed(0)


# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

# # Global Variables
# MAXRABBITPOP = 1000
# CURRENTRABBITPOP = 50
# CURRENTFOXPOP = 300


FOX_SUCCESS_REPRODUCTION_PROBABILITY = 1/3
FOX_FAIL_DEATH_PROBABILITY = 1/10
# FOX_FAIL_DEATH_PROBABILITY = 9/10


def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # Cacculate probablity for the rabitreproduction
    p_rrp = 1-(CURRENTRABBITPOP/MAXRABBITPOP)
    does_reproduce = np.random.random(int(CURRENTRABBITPOP))<=p_rrp
    temppop = CURRENTRABBITPOP+sum(does_reproduce)
    # Update the population of rabbit after reproduction
    CURRENTRABBITPOP = min(temppop, MAXRABBITPOP)




def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    global FOX_SUCCESS_REPRODUCTION_PROBABILITY
    global FOX_FAIL_DEATH_PROBABILITY

    if CURRENTFOXPOP>=10:
      if CURRENTRABBITPOP>=10:
        # Probability of a fox eating a rabbit
        p_fer = CURRENTRABBITPOP/MAXRABBITPOP
        fox_does_eat = np.random.random(CURRENTFOXPOP)<=p_fer
      else:
        fox_does_eat = np.zeros(CURRENTFOXPOP)

      # Number of fox which succeeded in eating a rabbit
      no_of_fox_success = int(sum(fox_does_eat))
      no_of_fox_fail = CURRENTFOXPOP - no_of_fox_success

      # Reduce the number of rabbit eaten
      rpop_eaten = sum(fox_does_eat)
      CURRENTRABBITPOP = max(10,CURRENTRABBITPOP-rpop_eaten)

      # All those foxes which were able to successfully eat a rabbit
      fox_does_reproduce = np.random.random(no_of_fox_success)<=FOX_SUCCESS_REPRODUCTION_PROBABILITY
      no_of_fox_reproduced = sum(fox_does_reproduce)
      # Update the total fox popultaion
      CURRENTFOXPOP += no_of_fox_reproduced

      
      # All those foxes which were unable to eat a rabbit
      fox_does_die = np.random.random(no_of_fox_fail)<=FOX_FAIL_DEATH_PROBABILITY
      no_of_fox_died = sum(fox_does_die)
      # Update the total fox popultaion
      CURRENTFOXPOP -= no_of_fox_died

            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    global CURRENTFOXPOP
    global CURRENTRABBITPOP

    fox_population, rabbit_population = [], []
    for _ in range(numSteps):
      # STEP 1 - RABBIT GROWTH
      rabbitGrowth()
      # STEP 2 - FOX GROWTH
      foxGrowth()

      fox_population.append(CURRENTFOXPOP)
      rabbit_population.append(CURRENTRABBITPOP)      

    return fox_population, rabbit_population


fpop, rpop = runSimulation(200)

plt.plot(fpop, label='Fox Population')
plt.plot(rpop, label='Rabbit Population')
plt.xlabel('Time Step')
plt.ylabel('Population')
plt.title('Variation in the Populations')
plt.legend()
plt.show()


# Polyfits
def fit_n_display(data, porder=2, title='Rabbit Population Fit'):
  model = np.polyfit(range(len(data)), data, porder)
  preds = np.polyval(model, range(len(data)))

  plt.scatter(range(len(data)), data, label = 'Actual Data', color='b')
  plt.plot(range(len(data)), preds, linestyle='-.', color='r', label = 'Fit Curve')
  plt.title(title)
  plt.legend()
  plt.show()


fit_n_display(rpop)
fit_n_display(fpop, title='Fox Population Fit')

