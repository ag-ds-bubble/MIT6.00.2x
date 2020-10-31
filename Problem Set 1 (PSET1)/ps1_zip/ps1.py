
###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time
import operator
from pprint import pprint

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def next_most_heavy(cows):
    return max(cows.copy().items(), key=operator.itemgetter(1))

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    tempCowDict = cows.copy()
    cowDict = cows.copy()
    trips = [[]]
    tripweight=0
    while len(cowDict) != 0:
        nextCow, nextCowWeight = next_most_heavy(cowDict)
        if tripweight+nextCowWeight<=limit:
            trips[-1].append(nextCow)
            tripweight += nextCowWeight
            del tempCowDict[nextCow]
        del cowDict[nextCow]
        if not cowDict:
            cowDict = tempCowDict.copy()
            tripweight = 0
            if tempCowDict!= {}:
                trips.append([])
    return trips
    

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowDict = cows.copy()
    all_partitions = list(get_partitions(cows.keys()))
    shortest_trips = 9999999
    shortest_trip = []
    for epart in all_partitions:
        if all(sum(cowDict[k] for k in etrip)<=limit for etrip in epart) and len(epart)<shortest_trips:
            shortest_trip = epart
            shortest_trips = len(epart)
    return shortest_trip
        
# Problem 3
def compare_cow_transport_algorithms(cows, limit):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    
    ts = time.perf_counter_ns()
    gct = greedy_cow_transport(cows, limit)
    print('GCT :->', gct)
    print(f'Time Taken by Greedy Algo : {round((time.perf_counter_ns()-ts)/1e9,3)} sec')

    ts = time.perf_counter_ns()
    bft = brute_force_cow_transport(cows, limit)
    print('BFT :->', bft)
    print(f'Time Taken by Brute Force Algo : {round((time.perf_counter_ns()-ts)/1e9,3)} sec')


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms(cows, 10)


