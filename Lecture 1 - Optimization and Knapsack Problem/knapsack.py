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
zippack = zip(['Wine', 'Beer', 'Pizza', 'Burger', 'Fries', 'Coke', 'Apple', 'Donut'],
              [89, 90, 30, 50, 90, 79, 90, 10],
              [123, 154, 258, 354, 365, 150, 95, 195])
food_menu = [Food(n,v,c) for n,v,c in zippack]
# pprint_foodm(food_menu)

def greedy(items, maxCost, keyFunction, keyFuncName):
    itemsCopy = sorted(items, key=keyFunction, reverse=True) # takes n*log(n) time
    optimal_selection = []
    totalValue, totalCost = 0, 0
    for i in range(len(itemsCopy)):
        if totalCost+itemsCopy[i].getCost() <= maxCost:
            optimal_selection.append(itemsCopy[i])
            totalValue+=itemsCopy[i].getValue()
            totalCost+=itemsCopy[i].getCost()
    print(f'For maxCost @ {maxCost} & keyFunc @ {keyFuncName} . Total Value : {totalValue} Total Calories : {totalCost}')
    pprint_foodm(optimal_selection)
    print('\n')

def test_greedys(max_cals):
    # By Value : Higher the Value the better
    greedy(food_menu, max_cals, lambda x : x.getValue(), 'By Value')

    # By Cost : Lower the calories the better
    greedy(food_menu, max_cals, lambda x : 1/x.getCost(), 'By Cost')

    # By Density : Higher the Value/Cost the better
    greedy(food_menu, max_cals, lambda x : x.getDensity(), 'By Density')
    

test_greedys(750)