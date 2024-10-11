import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
chars = sorted(list(map(str, input().split())))

vowels = set('aeiou')

answer = []

for comb in combinations(chars, l): # chars에서 l개의 조합 찾기
    count_vowel = sum(1 for char in comb if char in vowels)
    count_consonant = l - count_vowel

    if count_vowel >= 1 and count_consonant >= 2:
        answer.append(''.join(comb))

print(*answer, sep='\n')