import collections 
from aocd import get_data

data = get_data().splitlines()
lines = list(map(lambda x: list(map(int, x.split())), data))

for part in [1,2]:
    ans = 0
    for line in lines:
        if part == 2:
            all_lines = [line[:i] + line[i+1:] for i in range(len(line))]
        else:
            all_lines = [line]
        for mod_line in all_lines:
            prev = mod_line[0]
            mono = mod_line[0] > mod_line[1]
            for x in mod_line[1:]:
                if mono:
                    if prev <= x:
                        break
                else:
                    if prev >= x:
                        break
                if abs(prev - x) > 3:
                    break
                prev = x
            else:
                ans += 1
                break
    print(f"Part {part}:", ans)
