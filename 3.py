import re 
from aocd import get_data

data = "do()" + get_data()

matches = re.findall(r"mul\((\d+),(\d+)\)", data)
print("Part 1:", sum(int(x) * int(y) for x, y in matches))

results = []
segments = re.split(r"do\(\)", data)
if len(segments) > 1:  
    for segment in segments[1:]:
        segment_before_dont = re.split(r"don't\(\)", segment)[0]
        pattern_mul = r"mul\((\d+),(\d+)\)"
        matches = re.findall(pattern_mul, segment_before_dont)
        results.extend((int(x), int(y)) for x, y in matches)
print("Part 2:", sum(int(x) * int(y) for x, y in results))