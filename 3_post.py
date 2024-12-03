import re 
from aocd import get_data

data = "do()" + get_data()
p = r"mul\((\d+),(\d+)\)"
for part2 in [0, 1]:
    ans = 0
    flag = 0
    for i, c in enumerate(data):
        if data[i:].startswith("don't()"):
            flag = 0
        elif data[i:].startswith("do()"):
            flag = 1
        if flag or not part2:
            match = re.match(p, data[i:])
            if match is not None:
                a, b = map(int, match.groups())
                ans += a*b
    print(f"Part {part2 + 1}:", ans)