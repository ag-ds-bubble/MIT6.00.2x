import random
import itertools
import numpy as np
from warnings import filterwarnings
filterwarnings('ignore')


###################### HELPER FUNCTIONS #######################

class Item:
    def __init__(self, weight, value, desc):
        self.description = desc
        self.weight = np.float32(weight)
        self.value = np.float32(value)

    def __repr__(self):
        return self.description

    def get_metric1(self):
        return self.value/self.weight

    def get_metric2(self):
        return -self.weight

    def get_metric3(self):
        return self.value

def all_combinations(any_list):
    return itertools.chain.from_iterable(itertools.combinations(any_list, i) for i in range(len(any_list)+1))


######################## INITIALIZATION ########################
# L represents the list of items
zippack = zip(['Dirt', 'Computer', 'Fork', 'Problem Set'],
              [4, 10, 5, 0],
              [0, 30, 1, -10])
L = np.array([Item(weight=_weight, value=_value, desc=_desc) for _desc, _weight, _value in zippack])
random.shuffle(L)
# V represents the choosen items
V = np.zeros(len(L))
# CONSTRAINT
W = 14
print('List of all items : ', L)


######################## BRUTE FORCE ########################
optimal_val = 0
optimal_subset = []
all_combinations = list(itertools.product(range(2), repeat=4))
random.shuffle(all_combinations)
print('Setting a Base Line : ')
for ecomb in all_combinations:
    indexer = np.array(ecomb)==1
    choosen_items = L[indexer]
    total_weight = sum([k.weight for k in choosen_items])
    if total_weight <= W:
        total_value = sum([k.get_metric1() for k in choosen_items])
        if total_value>optimal_val:
            optimal_val = total_value
            optimal_subset = choosen_items
            print('\t',optimal_subset,' @ , W/V Ratio : ', total_value, '\n\t\tTotal Weight : ', total_weight, '\n\t\tTotal Value : ', sum([k.value for k in choosen_items]))


######################## WITH METRICS ########################
print('\n\n\n\nMetric Based -->')
for emetric in ['Metric1', 'Metric2', 'Metric3']:
    metric_vals = [getattr(eachItem, 'get_'+emetric.lower())() for eachItem in L]
    newlist = sorted(L, key=lambda x: getattr(x, 'get_'+emetric.lower())(), reverse=True)
    total_weight = 0
    optimal_items = []
    while newlist:
        optimal_items.append(newlist.pop(0))
        total_weight = sum(k.weight for k in optimal_items)
        if total_weight >= W:
            optimal_items.pop(-1)
            total_weight = sum(k.weight for k in optimal_items)
            
    print('Most optimal pick for the ', emetric, ' is : ', optimal_items, '. Total V/W : ', sum(k.get_metric1() for k in optimal_items))