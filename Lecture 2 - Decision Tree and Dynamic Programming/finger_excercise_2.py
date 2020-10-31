memo = {}
def forNthStep(n):
    if n in memo:
        return memo[n]
    else:
        if n <= 1: 
            return n
        res = forNthStep(n-1) + forNthStep(n-2)
        memo[n] = res
    return res
  
def countWays(s):
    return forNthStep(s + 1) 
  
# Driver program 
for i in [3, 5, 10, 120, 500, 1000]:
    print(f'Ways to reach {i}th step : ',countWays(i))
