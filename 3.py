import re 
from aocd import get_data

data = "do()" + get_data()
p = r"mul\((\d+),(\d+)\)"
matches = re.findall(p, data)
print("Part 1:", sum(int(x) * int(y) for x, y in matches))

ans = 0
segments = data.split("do()")
for segment in segments[1:]:
    segment_before_dont = segment.split("don't()")[0]
    matches = re.findall(p, segment_before_dont)
    for x, y in matches: ans += int(x) * int(y)
print("Part 2:", ans)