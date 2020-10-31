## Q1) Are the following two distributions equivalent?

```py
import random
def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 
```

- [x] Yes
- [ ] No

## Q2)Are the following two distributions equivalent?

```py
import random
def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)
```

- [x] Yes
- [ ] No

## Q3)Are the following two distributions equivalent?

```py
import random
def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)
```

- [ ] Yes
- [x] No
