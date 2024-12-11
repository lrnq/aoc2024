import collections
import itertools
from aocd import get_data

data = get_data().split()

def f(c):
    out = collections.Counter()
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
for i in range(75):
    cntr = f(cntr)
    if i in [24, 74]:
        print(sum(cntr[k] for k in cntr))