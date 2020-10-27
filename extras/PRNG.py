# Pseudo Random Number Generators
# 1.) Linear Congruential Generator
# 2.) Middle Squares Method
# 3.) Mersenne Twister

def middle_squares_method(seed=3187):
    num = seed
    while True:
        num = num**2
        yield int(str(num)[1:-1])

def linear_congruential_generator(a=13, b=4, m=101, seed=1):
    num = seed
    while True:
        num = (a*num+b)%m
        yield num

prng = linear_congruential_generator(2)

while True:
    print(next(prng))





