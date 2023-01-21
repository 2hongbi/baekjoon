def solution(array, n):
    temp = []
    array.sort()
    for arr in array:
        temp.append(abs(n - arr))
    return array[temp.index(min(temp))]