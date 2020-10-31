import random
import seaborn as sns
import matplotlib.pyplot as plt

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    evenlist = list(range(0, 100, 2))
    return random.choice(evenlist)

t = []
for _ in range(15000):
    t.append(genEven())

sns.displot(t)
plt.show()