from aocd import get_data

data = get_data().splitlines()
data = [list(x) for x in data]

n, m = len(data), len(data[0])
dirs = ((1,0),(-1,0),(0,1),(0,-1))

data_ = [[None for _ in range(2*m)] for _ in range(2*n)]
for i in range(n):
    for j in range(m):
        for di, dj in ((0, 0),(1, 0), (1, 1), (0, 1)):
            data_[2*i+di][2*j+dj] = data[i][j]

def perimeter_contribution(group, r, c):
    contribution = 0
    for dr, dc in dirs:
        if (not 0 <= r+dr < n) or (not 0 <= c+dc < m) or data[r+dr][c+dc] != group:
            contribution += 1
    return contribution

def corner(r, c, group):
    # convex case
    if (pc := perimeter_contribution(group, r, c)) == 2:
        return 1
    # concave case
    elif pc == 0:
        empty_corners = 0
        for dr, dc in ((1, 1), (-1, 1), (-1, -1), (1, -1)):
            empty_corners += data[r+dr][c+dc] != group
        return empty_corners == 1
    return 0
    
    

for part2 in [0, 1]:
    if part2:
        n,m = 2*n, 2*m
        data = data_
    seen = set()
    shapes = []
    for r in range(n):
        for c in range(m):
            if (r,c) not in seen:
                area, perimeter = 0, 0
                S = [(r,c)]
                seen.add((r,c))
                while S:
                    rr,cc = S.pop()
                    if not part2:
                        perimeter += perimeter_contribution(data[r][c], rr, cc)
                    else:
                        perimeter += corner(rr, cc, data[r][c])
                    area += 1
                    for dr, dc in dirs:
                        if (0 <= rr+dr < n) and (0 <= cc+dc < m) and data[rr+dr][cc+dc] == data[r][c]:
                            if (nxt := (rr+dr, cc+dc)) not in seen:
                                seen.add(nxt)
                                S.append(nxt)
                shapes.append((data[r][c], area, perimeter))

    agg = 0
    for x, y, z in shapes:
        if part2:
            y //=4
        agg += y*z
    print(agg)

        