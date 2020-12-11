# Quiz

### Problem 3
### You are given a list of unique positive integers L sorted in descending order and a positive integer sum s. The list has n elements. Consider writing a program that finds values for multipliers  m0,m1,...,mn−1  such that the following equation holds:  s=L[0]∗m0+L[1]∗m1+...+L[n−1]∗mn−1 
### Assume a greedy approach to this problem. You calculate the integer multipliers m_0, m_1, ..., m_(n-1) by finding the largest multiplier possible for the largest value in the list, then for the second largest, and so on. Write a function that returns the sum of the multipliers using this greedy approach. If the greedy approach does not yield a set of multipliers such that the equation above sums to s, return the string "no solution". Write the function implementing this greedy algorithm with the specification below:

```py
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    lsum = s
    mults = []
    for eelem in L:
        mults.append(lsum//eelem)
        lsum = lsum%eelem
    if lsum == 0:
        return sum(mults)
    else:
        return 'no solution'

```
### *Paste your entire function (including the definition) in the box. Do not leave any debugging print statements.*