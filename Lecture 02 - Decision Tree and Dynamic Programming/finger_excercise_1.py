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
zippack = zip(['Wine', 'Beer', 'Pizza', 'Burger', 'Fries', 'Coke', 'Apple', 'Donut'],
              [89, 90, 30, 50, 90, 79, 90, 10],
              [123, 154, 258, 354, 365, 150, 95, 195])
food_menu = [Food(n,v,c) for n,v,c in zippack]

def dec2base(x, base):
    num = []
    remainder = None
    while x:
        x, remainder = divmod(x,base)
        num.append(remainder)
    return np.array(num)

def powerSetTernary(items):
    items = np.array(items).copy()
    N = len(items)
    for i in range(3**N):
        base3repr = dec2base(i, 3)
        if len(base3repr) != N:
            base3repr = np.append(base3repr, [0]*(N-len(base3repr)))
        yield items[base3repr==1].tolist(), items[base3repr==2].tolist()


pset_gen = powerSetTernary(food_menu)
print('Total Number of combination sets : ', len(list(pset_gen)))
pset_gen = powerSetTernary(food_menu)

for i in range(10):
    print(next(pset_gen))
