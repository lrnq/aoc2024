import collections 
from aocd import get_data

data = get_data().split("\n")
l1, l2 = [], []
for row in data: 
    a, b = map(int, row.split("   "))
    l1.append(a); l2.append(b)


l1.sort(); l2.sort()

print("Part 1:", sum(abs(x-y) for x, y in zip(l1, l2)))

cnts = collections.Counter(l2)
print("Part 2:", sum(x * cnts[x] for x in l1))

