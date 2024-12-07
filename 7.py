import collections
import itertools
from aocd import get_data

data = get_data().splitlines()
ops = ["*", "+", "|"]
d = collections.defaultdict(list)
for line in data:
    ans, nums = line.split(":")
    ans = int(ans)
    for n in nums.strip().split():
        d[ans].append(int(n))

def good(nums, ans, part2):
    if len(nums) == 1:
        return nums.pop() == ans
    if good([nums[0] + nums[1]] + nums[2:], ans, part2):
        return True
    if good([nums[0] * nums[1]] + nums[2:], ans, part2):
        return True
    if part2:
        if good([int(str(nums[0]) + str(nums[1]))] + nums[2:], ans, part2):
            return True
    return False

    

print("Part 1:", sum(ans for ans, nums in d.items() if good(nums, ans, False)))
print("Part 2:", sum(ans for ans, nums in d.items() if good(nums, ans, True)))