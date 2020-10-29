### Q.1) Dynamic programming can be used to solve optimization problems where the size of the space of possible solutions is exponentially large?

- [x] True
- [ ] False

### Q.2) Dynamic programming can be used to find an approximate solution to an optimization problem, but cannot be used to find a solution that is guaranteed to be optimal.

- [ ] True
- [x] False

### Q.3) Recall that sorting a list of integers can take  O(nlogn)  using an algorithm like merge sort. Dynamic programming can be used to reduce the order of algorithmic complexity of sorting a list of integers to something below  nlogn , where n is the length of the list to be sorted.

- [ ] True
- [x] False

### Q.3) Problem: I need to go up a flight of  N  stairs. I can either go up 1 or 2 steps every time. How many different ways are there for me to traverse these steps? For example:
```
    3 steps -> could be 1,1,1 or 1,2 or 2,1
    4 steps -> could be 1,1,1,1 or 1,1,2 or 1,2,1 or 2,1,1 or 2,2
    5 steps -> could be 1,1,1,1,1 or 1,1,1,2 or 1,1,2,1 or 1,2,1,1 or 2,1,1,1 or 2,2,1 or 1,2,2 or 2,1,2
```
Does this problem have optimal substructure and overlapping subproblems?

- [x] It has optimal substructure and overlapping subproblems
- [ ] It doe not have optimal substructure and does not have overlapping subproblems
- [ ] It has optimal substructure and does not have overlapping subproblems
- [ ] It does not have optimal substructure and it has overlapping subproblems
