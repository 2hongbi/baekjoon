s = input()
alphabet = [-1] * 26
for i in range(len(s)):
    ch = ord(s[i])

    if alphabet[ch - 97] == -1:
        alphabet[ch - 97] = i

for i in alphabet:
    print(i, end=' ')