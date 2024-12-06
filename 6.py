import collections
import itertools
from aocd import get_data

data = [list(x) for x in get_data().splitlines()]
for k, line in enumerate(data):
    if "^" in line:
        start = line.index("^")
        break

d = {(-1, 0): (0, 1),(0, 1): (1, 0),(1, 0): (0, -1),(0, -1): (-1, 0)}

def inside(y, dy, x, dx):
    return 0 <= x + dx < len(data) and 0 <= y + dy < len(data[0])


x, y = k, start
dx, dy = (-1, 0)
seen = set()
while 1:
    seen.add((x,y))
    if not inside(y, dy, x, dx):
        break
    if data[x+dx][y+dy] in [".", "^"]:
        x += dx
        y += dy
    else:
        while data[x+dx][y+dy] not in [".", "^"]:
            dx, dy = d[(dx, dy)]
        if not inside(y, dy, x, dx):
            break
        x += dx
        y += dy

print("Part 1:", len(seen))

# Copy paste the above and run a simulation. 
ans = 0
for cntr, (i,j) in enumerate(seen):
    print(f"{cntr}/{len(seen)}")
    if data[i][j] != "^":
        data[i][j] = "#"
        dx, dy = (-1, 0)
        x, y = k, start
        seen_ = collections.defaultdict(int)
        while 1:
            seen_[(x,y)] += 1
            if seen_[(x,y)] > 4:
                ans += 1
                break
            if not inside(y, dy, x, dx):
                break
            if data[x+dx][y+dy] in [".", "^"]:
                x += dx
                y += dy
            else:
                while data[x+dx][y+dy] not in [".", "^"]:
                    dx, dy = d[(dx, dy)]
                if not inside(y, dy, x, dx):
                    break
                x += dx
                y += dy
        data[i][j] = "."
print("Part 2:", ans)