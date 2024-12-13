from aocd import get_data
from sympy import solve
from sympy.abc import A, B

# Initially i just did some heuristics based + DP solution for part 1, 
# but it was too slow for part 2 even when i tried to optimize with GCD of 
# the individual largest proper divisors - the input looked like it was purposefully
# designed this way. Evenutally i realized it is just some linear algebra.
# I wanted to use sympy for something though before i suspect it will be needed 
# for later days.
data = get_data().split("\n\n")
for part2 in [0, 1]:
    agg = 0
    for i, group in enumerate(data):
        lines = group.splitlines()
        ax, ay = [int(x.strip()[2:]) for x in lines[0].split(":")[-1].split(",")]
        bx, by = [int(x.strip()[2:]) for x in lines[1].split(":")[-1].split(",")]
        px, py = [int(x.strip()[2:]) for x in lines[2].split(":")[-1].split(",")]
        if part2:
            px, py = px+10000000000000, py+10000000000000

        sol = solve([A*ax+B*bx-px, A*ay+B*by-py], [A, B])
        if sol[A].is_Integer and sol[B].is_Integer:
            agg += sol[A]*3 + sol[B]
    print(agg)
