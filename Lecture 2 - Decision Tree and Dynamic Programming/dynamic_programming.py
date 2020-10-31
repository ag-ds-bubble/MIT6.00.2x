import numpy as np
class Food:
    def __init__(self, n, v, c):
        self.name = n
        self.value = v
        self.calories = c

    def __str__(self):
        return self.name + f': <V:{self.value}, C:{self.calories}>'

    def __repr__(self):
        return self.name + f': <V:{self.value}, C:{self.calories}>'
    
    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def getDensity(self):
        return self.getValue()/self.getCost()

def pprint_foodm(fmlist):
    for k in fmlist:
        print('\t', k.__str__())

# Building Menu
with open('../Raw Data/food_items.txt', 'r') as f:
    food_names = f.readlines()
food_names = [k.strip().capitalize() for k in food_names]*2
zippack = zip(food_names,
              np.random.uniform(10, 150, size=len(food_names)).astype(int),
              np.random.uniform(10, 150, size=len(food_names)).astype(int))
food_menu = [Food(n,v,c) for n,v,c in zippack]

def maxVal(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0,())
    elif toConsider[0].getCost()>avail:
        result=maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail-nextItem.getCost())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake+(nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def fastMaxVal(toConsider, avail, memo = {}):
    global t
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0,())
    elif toConsider[0].getCost()>avail:
        result=fastMaxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = fastMaxVal(toConsider[1:], avail-nextItem.getCost())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake+(nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

def test_runs(max_cals):
    # for itemcounts in list(range(5,55,5)):
    #     print(f'Running for {itemcounts} items menu.')
    #     tempmenu = food_menu[:itemcounts]
    #     # Search Tree - Two Constraint
    #     totalValue, items = maxVal(tempmenu, max_cals)
    #     totalCost = sum(k.getCost() for k in items)
    #     print(f'Search Tree Solution :: For maxCost @ {max_cals} . Total Value : {totalValue} Total Calories : {totalCost}')
    #     # pprint_foodm(items)
    #     print('\n')
    
    for itemcounts in list(range(5,55,5)):
        print(f'Running for {itemcounts} items menu.')
        tempmenu = food_menu[:itemcounts]
        # Search Tree - Two Constraint
        totalValue, items = fastMaxVal(tempmenu, max_cals)
        totalCost = sum(k.getCost() for k in items)
        print(f'Search Tree Solution :: For maxCost @ {max_cals} . Total Value : {totalValue} Total Calories : {totalCost}, Number of calls ', t)
        print('\n')

test_runs(750)