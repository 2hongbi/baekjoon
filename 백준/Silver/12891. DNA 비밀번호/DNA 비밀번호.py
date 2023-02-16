import sys
input = sys.stdin.readline
s, p = map(int, input().split())  # 임의, 비번
dna_string = list(input().rstrip())
dna = [0, 0, 0, 0]
min_num = list(map(int, input().split()))  # A, C, G ,T
start, end = 0, p
count = 0


def dna_count(start, end):
    global count,DNA
    for i in range(start, end):
        if dna_string[i] == 'A':
            dna[0] += 1
        elif dna_string[i] == 'C':
            dna[1] += 1
        elif dna_string[i] == 'G':
            dna[2] += 1
        else:
            dna[3] += 1
    if (dna[0] >= min_num[0]) and (dna[1] >= min_num[1]) and (dna[2] >= min_num[2]) and (dna[3] >= min_num[3]):
        count += 1


dna_count(start, end)
for i in range(end, s):
    if dna_string[i] == 'A':
        dna[0] += 1
    elif dna_string[i] == 'C':
        dna[1] += 1
    elif dna_string[i] == 'G':
        dna[2] += 1
    elif dna_string[i] == 'T':
        dna[3] += 1

    if dna_string[i-p] == 'A':
        dna[0] -= 1
    elif dna_string[i-p] == 'C':
        dna[1] -= 1
    elif dna_string[i-p] == 'G':
        dna[2] -= 1
    elif dna_string[i-p] == 'T':
        dna[3] -= 1
    if (dna[0] >= min_num[0]) and (dna[1] >= min_num[1]) and (dna[2] >= min_num[2]) and (dna[3] >= min_num[3]):
        count += 1

print(count)