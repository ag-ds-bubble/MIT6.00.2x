import random
import seaborn as sns
import matplotlib.pyplot as plt

def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1

def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)

def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)


fig, axes = plt.subplots(3,2)
for idx, packet in enumerate(zip([dist1, dist3, dist5], [dist2, dist4, dist6])):
    ldist, rdist = packet
    d1 = [ldist() for _ in range(100000)]
    d2 = [rdist() for _ in range(100000)]
    sns.histplot(d1, ax=axes[idx][0], kde=True)
    sns.histplot(d1, ax=axes[idx][1], kde=True)
plt.show()