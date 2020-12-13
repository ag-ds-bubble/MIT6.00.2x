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

# SEARCH TREE
class Leaf:
    def __init__(self, itemList, leftChid, rightChild):
        self.inleafItems = itemList
        self.leftChild = leftChid
        self.rightChild = rightChild

        self.leafCost = 0
        self.leafValue = 0


def buildTree(unSelectedItems, maxCost, selectedItems=[], currCost=0):
    print('Building Search Tree for ', maxCost)
    pprint_foodm(unSelectedItems)
    pprint_foodm(selectedItems)
    
    if currCost+unSelectedItems[0].getCost() < maxCost:
        


    Leaf(selectedItems, Leaf())

buildTree(food_menu, 750)