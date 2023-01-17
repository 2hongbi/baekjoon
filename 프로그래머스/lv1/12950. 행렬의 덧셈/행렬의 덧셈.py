def solution(arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        temp = []
        for i, j in zip(a1, a2):
            temp.append(i+j)
        answer.append(temp)
    return answer