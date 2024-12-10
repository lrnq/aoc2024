import collections
import itertools
from aocd import get_data

data = [list(x) for x in get_data().splitlines()]
n, m = len(data), len(data[0])


def collinear(p0, p1, p2):
    x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
    x2, y2 = p2[0] - p0[0], p2[1] - p0[1]
    return abs(x1 * y2 - x2 * y1) < 1e-12

seen = set()
for i in range(n):
    for j in range(m):
        if data[i][j] == ".": continue
        for ii in range(n):
            for jj in range(m):
                if ((i,j) != (ii,jj)) and (data[i][j] == data[ii][jj]):
                    dr, dc = abs(i - ii), abs(j-jj)
                    flag = 0
                    iter = 1
                    prev_seen = seen.copy()
                    while 1:
                        if 0 <= ii+dr*iter < n and 0 <= jj+dc*iter < m:
                            if collinear((ii+dr*iter,jj+dc*iter), (i,j), (ii,jj)):
                                seen.add((ii+dr*iter, jj+dc*iter))
                        if 0 <= ii-dr*iter < n and 0 <= jj-dc*iter < m:
                            if collinear((ii-dr*iter,jj-dc*iter), (i,j), (ii,jj)):
                                seen.add((ii-dr*iter, jj-dc*iter))
                        if 0 <= ii+dr*iter < n and 0 <= jj-dc*iter < m:
                            if collinear((ii+dr*iter,jj-dc*iter), (i,j), (ii,jj)):
                                seen.add((ii+dr*iter, jj-dc*iter))
                        if 0 <= ii-dr*iter < n and 0 <= jj+dc*iter < m:
                            if collinear((ii-dr*iter,jj+dc*iter), (i,j), (ii,jj)):
                                seen.add((ii-dr*iter, jj+dc*iter))
                        if len(seen) == len(prev_seen):
                            flag += 1
                            if flag > 25:
                                break
                        prev_seen = seen.copy()
                        iter += 1

print(len(seen))

