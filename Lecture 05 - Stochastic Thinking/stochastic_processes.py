import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def testRoll(n=10):
    res = ''
    for _ in range(n):
        res += str(rollDie())
    print(res)

for _ in range(100):
    testRoll()