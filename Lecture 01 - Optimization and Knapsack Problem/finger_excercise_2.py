class Item:
    def __init__(self, n, v, c):
        self.name = n
        self.value = v
        self.weight = c

    def __str__(self):
        return self.name + f': <V:{self.value}, C:{self.weight}>'

    def __repr__(self):
        return self.name + f': <V:{self.value}, C:{self.weight}>'
    
    def getValue(self):
        return self.value

    def getCost(self):
        return self.weight

    def getDensity(self):
        return self.getValue()/self.getCost()

def pprint_item(fmlist):
    for k in fmlist:
        print('\t', k.__str__())

# Building Menu
zippack = zip(['Clock', 'Picture', 'Radio', 'Vase', 'Book', 'Computer'],
              [175, 90, 20, 50, 10, 200],
              [10, 9,4, 2, 1, 20])
all_items = [Item(n,v,w) for n,v,w in zippack]
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
    print(f'For maxCost @ {maxCost} & keyFunc @ {keyFuncName} . Total Value : {totalValue} Total weight : {totalCost}')
    pprint_item(optimal_selection)
    print('\n')

def test_greedys(max_cals):
    # By Value : Higher the Value the better
    greedy(all_items, max_cals, lambda x : x.getValue(), 'By Value')

    # By Cost : Lower the weight the better
    greedy(all_items, max_cals, lambda x : 1/x.getCost(), 'By Weight')

    # By Density : Higher the Value/Cost the better
    greedy(all_items, max_cals, lambda x : x.getDensity(), 'By Density')
    

test_greedys(20)