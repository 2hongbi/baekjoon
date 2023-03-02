import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
card_dict = defaultdict(int)

tmp = list(map(int, input().split()))
for t in tmp:
    card_dict[t] += 1

m = int(input())
check_list = list(map(int, input().split()))
tmp = []
for check in check_list:
    if check in card_dict.keys():
        tmp.append(str(card_dict[check]))
    else:
        tmp.append('0')

print(' '.join(tmp))