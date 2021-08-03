# combinations
from itertools import combinations

candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combi = combinations(candidate, 7)
for i in combi:
    print(i)
