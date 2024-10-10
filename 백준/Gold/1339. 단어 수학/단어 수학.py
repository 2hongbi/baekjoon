from collections import defaultdict

n = int(input())
words = [input().strip() for _ in range(n)]

char_weight = defaultdict(int)
for word in words:
    length = len(word)
    for i, char in enumerate(word):
        weight = 10 ** (length - i - 1)
        char_weight[char] += weight


sorted_chars = sorted(char_weight.items(), key=lambda x: x[1], reverse=True)

value = 9
char_to_num = {}
for char, _ in sorted_chars:
    char_to_num[char] = value
    value -= 1

total_sum = 0
for word in words:
    num_value = ''
    for char in word:
        num_value += str(char_to_num[char])
    total_sum += int(num_value)

print(total_sum)