import collections
import more_itertools
from aocd import get_data

pairs = list(more_itertools.batched(get_data().splitlines(), 2))

# Not great, but the input is small.
explicit = []
for id, p in enumerate(pairs):
    p = tuple(map(int, p))
    for j in range(p[0]):
        explicit.append(id)
    if len(p) > 1:
        for j in range(p[1]):
            explicit.append(".")

def get_block_to_move(explicit, start):
    while start >= 0 and explicit[start] == ".":
        start -= 1
    id_to_move = start
    ids = []
    while 0 <= id_to_move and explicit[id_to_move] == explicit[start]:
        ids.append(id_to_move)
        id_to_move -= 1
    return ids

block_to_move = get_block_to_move(explicit, len(explicit)-1)
while 1:
    if block_to_move == []: break
    i = 0
    while i < len(explicit):
        c = explicit[i]
        if c == ".":
            j, l = i, 0
            while j < len(explicit) and explicit[j] == ".":
                l += 1
                j += 1
            if (j - i) >= len(block_to_move):
                x = i
                for k in block_to_move:
                    if k > x:
                        explicit[k], explicit[x] = explicit[x], explicit[k]
                    x += 1
                break
        i += 1
    block_to_move = get_block_to_move(explicit, min(block_to_move)-1)

sum(i*c for i, c in enumerate(explicit) if c != ".")
