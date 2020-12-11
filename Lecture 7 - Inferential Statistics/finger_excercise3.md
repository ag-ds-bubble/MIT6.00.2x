## Finger Excercise 3
### Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and outputs the standard deviation of the lengths of the strings. Return float('NaN') if L is empty.

### Recall that the standard deviation is computed by this equation:

###  ∑t in X(t−μ)2N−−−−−−−−−−−−−√ 
### where:

### μ  is the mean of the elements in X.

### ∑t in X(t−μ)2  means the sum of the quantity  (t−μ)2  for t in X.

### That is, for each element (that we name t) in the set X, we compute the quantity  (t−μ)2 . We then sum up all those computed quantities.

### N is the number of elements in X.

### Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.

### Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], stdDevOfLengths(L) should return 1.8708.

```py
import math
def stdDevOfLengths(L):
    if L==[]: return float('NaN')
    _lL = [len(k) for k in L]
    _mean = sum(_lL)/len(_lL)
    _std = math.sqrt(sum([(k-_mean)**2 for k in _lL])/len(_lL))
    return _std
```