import string


def solution(age):
    age_list = list(string.ascii_lowercase)
    answer = [age_list[i] for i in list(map(int, str(age)))]
    return ''.join(answer)