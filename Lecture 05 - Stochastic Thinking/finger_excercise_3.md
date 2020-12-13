## Exercise 3-1

### Q1) Write a deterministic program, deterministicNumber, that returns an even number between 9 and 21.
```py
import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(0)
    return random.randrange(10, 22, 2)
```


## Exercise 3-2
### Q2) Write a uniformly distributed stochastic program, stochasticNumber, that returns an even number between 9 and 21.
```py
import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10, 22, 2)
```