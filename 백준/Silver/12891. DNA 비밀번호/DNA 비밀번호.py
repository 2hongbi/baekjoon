import sys
from collections import Counter

input = sys.stdin.readline

s, p = map(int, input().split())
dna_string = input().strip()
min_count = list(map(int, input().split())) # minimum count of a, c, g, t

current_count = Counter(dna_string[:p])

def is_valid():
    return (current_count['A'] >= min_count[0] and
            current_count['C'] >= min_count[1] and
            current_count['G'] >= min_count[2] and
            current_count['T'] >= min_count[3])

answer = 0

if is_valid():
    answer += 1


for i in range(1, s - p + 1):
    prev_char = dna_string[i - 1]
    next_char = dna_string[i + p - 1]

    current_count[prev_char] -= 1
    current_count[next_char] += 1

    if is_valid():
        answer += 1

print(answer)