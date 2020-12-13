from time import perf_counter_ns
import matplotlib.pyplot as plt


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

memo = {}
def fibMemo(n):
    try :
        return memo[n]
    except:
        _fib = 0
        if n == 0 or n == 1:
            _fib = 1
        else:
            _fib = fibMemo(n-2)+fibMemo(n-1)
        memo[n] = _fib
        return _fib


x=[]
y=[]
for i in range(130):
    ts = perf_counter_ns()
    calc = fib(i)
    ttaken = round((perf_counter_ns()-ts)/1e9, 3)
    print(f'fib({i}) = {calc}. Time Taken {ttaken} sec')
    x.append(i)
    y.append(ttaken)
    if ttaken>20:
        break

plt.plot(x,y)
plt.title('Time taken for Recurrsive Fibonacci.')
plt.show()


x=[]
y=[]
for i in range(130):
    ts = perf_counter_ns()
    calc = fibMemo(i)
    ttaken = round((perf_counter_ns()-ts)/1e9, 3)
    print(f'fib({i}) = {calc}. Time Taken {ttaken} sec')
    x.append(i)
    y.append(ttaken)
    if ttaken>20:
        break

plt.plot(x,y)
plt.title('Time taken for Fibonacci (DP)')
plt.show()
