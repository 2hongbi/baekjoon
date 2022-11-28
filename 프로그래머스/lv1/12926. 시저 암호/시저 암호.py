def solution(s, n):
    answer = ''
    for c in s:
        if c.isspace():
            answer += ' '
        elif c.isupper():  # 알파벳 26개, 인덱스 0 ~ 25이므로, 25 넘어간 경우 처리
            answer += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        elif c.islower():
            answer += chr((ord(c) - ord('a') + n) % 26 + ord('a'))

    return answer