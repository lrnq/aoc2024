import collections 
from aocd import get_data

data = get_data().split("\n")
l1, l2 = [], []
for row in data: 
    a, b = map(int, row.split("   "))
    l1.append(a); l2.append(b)


l1.sort(); l2.sort()

ans1 = 0
for x, y in zip(l1, l2):
    ans1 += abs(x-y)
print("Part 1:", ans1)

cnts = collections.Counter(l2)
ans2 = 0
for x in l1:
    ans2 += x * cnts[x]
print("Part 2:", ans2)

