from collections import Counter

s, p = map(int, input().split()) # dna 문자열 길이, 비밀번호로 사용할 부분문자열의 길이
dna_string = input()
min_count = list(map(int, input().split())) # 부분 문자열에 포함되어야 할 A, C, G, T의 최소 개수

# 현재 윈도우 내의 각 문자 빈도수 카운터
current_count = Counter(dna_string[:p])

def is_valid():
    return (current_count['A'] >= min_count[0] and
            current_count['C'] >= min_count[1] and
            current_count['G'] >= min_count[2] and
            current_count['T'] >= min_count[3])


valid_password = 0
# 첫 번째 윈도우 검사
if is_valid():
    valid_password += 1

for i in range(1, s - p + 1):
    prev_char = dna_string[i - 1]
    current_count[prev_char] -= 1

    # 새문자 추가
    new_char = dna_string[i + p - 1]
    current_count[new_char] += 1

    if is_valid():
        valid_password += 1

print(valid_password)