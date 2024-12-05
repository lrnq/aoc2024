import collections
import itertools
from aocd import get_data

data = get_data().split("\n\n")
ordering, lines = data 
ordering = set(tuple(map(int, line.split("|"))) for line in ordering.splitlines())
lines = [list(map(int, line.split(","))) for line in lines.splitlines()]


ans = 0
bad = []
for line in lines:
    for x in itertools.pairwise(line):
        if x not in ordering:
            bad.append(line)
            break
    else:
        ans += line[len(line)//2]
print("Part 1:", ans)

ordering_d = collections.defaultdict(set)
for x, y in ordering: ordering_d[x].add(y)

ans = 0
for line in bad:
    for i in range(1, len(line)):
        k = line[i]
        j = i - 1 
        while j >= 0 and line[j] not in ordering_d[k]:
            line[j+1] = line[j]
            j -= 1
        line[j+1] = k
    ans += line[len(line)//2]
print("Part 2:", ans)