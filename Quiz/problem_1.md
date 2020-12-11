# Quiz

### Q 1-1) The following function is stochastic:
```py
def f(x):
    # x is an integer
    return int(x + random.choice([0.25, 0.5, 0.75]))
```
- [ ] True
- [x] False

### Q 1-2) In Python, we can use random.seed(100) at the beginning of a program to generate the same sequence of random numbers each time we run a program.

- [x] True
- [ ] False

### Q 1-3) A brute force solution to the 0/1 knapsack problem will always produce an optimal solution.

- [x] True
- [ ] False

### Q 1-5) Consider an undirected graph with non-negative weights that has an edge between each pair of nodes. The shortest distance between any two nodes is always the path that is the edge between the two nodes.

- [ ] True
- [x] False
*Hint : Read carefully that the weights are non-negative BUT not non-existent, so the sortest path will also have a factor of sum weights to take into account*