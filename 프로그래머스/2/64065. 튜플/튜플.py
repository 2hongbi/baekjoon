def solution(s):
    data = s[2:-2].split('},{')
    data = sorted(data, key=lambda x: len(x))
    answer = []
    for d in data:
        d = list(map(int, d.split(',')))
        for value in d:
            if value not in answer:
                answer.append(value)
    return answer