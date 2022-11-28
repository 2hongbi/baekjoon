def solution(n, arr1, arr2):
    answer = []
    for one, two in zip(arr1, arr2):
        temp = ''
        one = bin(one)[2:].zfill(n)
        two = bin(two)[2:].zfill(n)
        for i in range(n):
            if one[i] == '0' and two[i] == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer