import collections
import itertools
from aocd import get_data

data = get_data().split()

def f(c):
    out = collections.defaultdict(int)
    for k, v in c.items():
       if k == "0":
           out["1"] += v
       elif len(k) % 2 == 0:
            out[str(int(k[:len(k)//2]))] += v 
            out[str(int(k[len(k)//2:]))] += v 
       else:
           out[str(int(k) * 2024)] += v
    return out

cntr = collections.Counter(data)
for _ in range(25):
    cntr = f(cntr)
print(sum(cntr[k] for k in cntr))

cntr = collections.Counter(data)
for _ in range(75):
    cntr = f(cntr)
print(sum(cntr[k] for k in cntr))