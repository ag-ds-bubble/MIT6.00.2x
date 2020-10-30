import matplotlib.pyplot as plt
import random
from time import perf_counter

NUMBER = 3
x=[]
y=[]
univ = list(range(10000))

def look_for_things(myList):
    """Looks at all elements"""
    for n in myList:
        if n == NUMBER:
            return True
    return False

def look_for_other_things(myList):
    """Looks at all pairs of elements"""
    for n in myList:
        for m in myList:
            if n - m == NUMBER or m - n == NUMBER:
                return True
    return False

def get_all_subsets(some_list):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets

def look_for_all_the_things(myList):
    """Looks at all subsets of this list"""
    # Make subsets
    all_subsets = get_all_subsets(myList)
    for subset in all_subsets:
        if sum(subset) == NUMBER:
            return True
    return False

x, y=[], []
for i in range(int(1e3)):
    population = random.sample(univ, i)
    ts = perf_counter()
    look_for_things(population)
    x.append(i)
    y.append(perf_counter()-ts)

plt.scatter(x,y,s=1)
plt.show()

x, y=[], []
for i in range(int(1e3)):
    population = random.sample(univ, i)
    ts = perf_counter()
    look_for_other_things(population)
    x.append(i)
    y.append(perf_counter()-ts)

plt.scatter(x,y,s=1)
plt.show()

x, y=[], []
for i in range(int(20)):
    x.append(i)
    population = random.sample(univ, i)
    ts = perf_counter()
    look_for_all_the_things(population)
    y.append(perf_counter()-ts)

plt.scatter(x,y,s=2)
plt.show()
