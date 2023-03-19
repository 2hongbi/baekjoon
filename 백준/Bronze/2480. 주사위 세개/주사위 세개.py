import sys
from collections import Counter
input = sys.stdin.readline

nums = list(map(int, input().split()))
same_nums = list(set(nums))

if len(same_nums) == 1:
    print(10000 + same_nums[0] * 1000)
elif len(same_nums) == 2:
    cnt = Counter(nums)
    print(1000 + cnt.most_common(1)[0][0] * 100)
else:
    print(max(nums) * 100)