### As a burgler robs a house, she finds the following items:

- Dirt - Weight: 4, Value: 0
- Computer - Weight: 10, Value: 30
- Fork - Weight: 5, Value: 1
- Problem Set - Weight: 0, Value: -10

### This time, she can only carry a weight of 14, and wishes to maximize the value to weight ratio of the things she carries. She employs three different metrics in an attempt to do this, and writes an algorithm in Python to determine which loot to take.

### The algorithm works as follows:
### Evaluate the metric of each item. Each metric returns a numerical value for each item.
### For each item, from highest metric value to lowest, add the item if there is room in the bag.
### Describe the heuristic that each of the following 3 metrics uses, and choose the result of running the algorithm with each metric.


### **Q1)** Metric 1:

    def metric1(item):
        return item.getValue() / item.getWeight()
**Q1.1)** Which heuristic does Metric 1 employ?


- [ ] Choose the lightest object first.
- [ ] Choose the most valuable object first.
- [x] Choose the item with the best value to weight ratio first.


**Q1.2)** What will be the result of running the burgler's algorithm with Metric 1?


- [ ] The algorithm runs and returns the optimal solution.
- [ ] The algorithm runs and returns a non-optimal solution.
- [x] The algorithm does not run.

### **Q1)** Metric 2:

    def metric2(item):
        return  -item.getWeight()
**Q2.1)** Which heuristic does Metric 2 employ?


- [x] Choose the lightest object first.
- [ ] Choose the most valuable object first.
- [ ] Choose the item with the best value to weight ratio first.

**Q2.2)** What will be the result of running the burgler's algorithm with Metric 2?


- [ ] The algorithm runs and returns the optimal solution.
- [x] The algorithm runs and returns a non-optimal solution.
- [ ] The algorithm does not run.

### **Q1)** Metric 3:

    def metric3(item):
        return item.getValue()
**Q3.1)** Which heuristic does Metric 3 employ?


- [ ] Choose the lightest object first.
- [x] Choose the most valuable object first.
- [ ] Choose the item with the best value to weight ratio first.

**Q3.2)** What will be the result of running the burgler's algorithm with Metric 3?


- [ ] The algorithm runs and returns the optimal solution.
- [x] The algorithm runs and returns a non-optimal solution.
- [ ] The algorithm does not run.