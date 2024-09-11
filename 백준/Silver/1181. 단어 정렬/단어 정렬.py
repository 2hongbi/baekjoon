import sys
input = sys.stdin.readline

n = int(input())
words = set(input().strip() for _ in range(n))

# sort by length of words, then lexicographic
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)