import random
import seaborn as sns
import matplotlib.pyplot as plt

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    pass

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10, 22, 2)



t = []
for _ in range(5000):
    if stochasticNumber()%2:
        print('fail')
    t.append(stochasticNumber())
sns.displot(t)
plt.show()