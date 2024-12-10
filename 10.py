import collections
import itertools
from aocd import get_data

grid = [list(map(int, list(x))) for x in get_data().splitlines()]
n, m = len(grid), len(grid[0])

G = collections.defaultdict(list)
start_nodes = []
for i in range(n):
    for j in range(m):
        e = grid[i][j]
        if not e:
            start_nodes.append((e,i,j))
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0,-1)]:
            if 0 <= i+dr < n and 0 <= j+dc < m:
                G[(e,i,j)].append((grid[i+dr][j+dc], i+dr, j+dc))

for part2 in [0, 1]:
    ans = 0
    for node in start_nodes:
        S = [(node, [node])]
        seen = set()
        while S:
            node, path = S.pop()
            if node[0] == 9:
                ans += 1
            for x in G[node]:
                if x[0] == node[0]+1:
                    if part2:
                        if not (t := tuple(path + [x])) in seen:
                            seen.add(t)
                            S.append((x, list(t)))
                    else:
                        if not x in seen:
                            seen.add(x)
                            S.append((x, path))
    print(ans)
            

        
        

