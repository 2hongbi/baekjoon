def solution(arr1, arr2):
    answer = []
    tarr2 = list(map(list, zip(*arr2)))
    for i in range(len(arr1)):
        temp = []
        for j in range(len(tarr2)):
            temp.append(sum([a * b for a, b in zip(arr1[i], tarr2[j])]))
        answer.append(temp)
    return answer