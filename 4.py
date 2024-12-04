import numpy as np
from aocd import get_data

data = get_data().splitlines()
rows = np.array(list(map(list, data)))
m, n = rows.shape
cols = rows.T
diag = [rows.diagonal(x) for x in range(-m, n)]
anti_diag = [rows[...,::-1].diagonal(x) for x in range(-m, n)]

def count(arr):
    return sum(''.join(x).count("XMAS") + ''.join(x).count("SAMX") for x in arr)

print("Part 1:", count(rows) + count(cols) + count(diag) + count(anti_diag))


# Probably there is some clever way to match for "MAS" and "SAM"
# in the diagonal and anti-diagonal and check if the "A" is at the same index.
ans = 0
for i in range(1, m-1):
    for j in range(1, n-1):
        if rows[i,j] == "A":
            d_ = sorted([rows[i+1, j+1], "A", rows[i-1, j-1]])
            d  = sorted([rows[i-1, j+1], "A", rows[i+1, j-1]])
            ans += "".join(d) == "AMS" and "".join(d_) == "AMS"
print("Part 2:", ans)