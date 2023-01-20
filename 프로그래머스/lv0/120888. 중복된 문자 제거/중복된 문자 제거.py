def solution(my_string):
    answer = ''
    for st in my_string:
        if st not in answer:
            answer += st
    return answer