def solution(answers):
    pat1 = [1, 2, 3, 4, 5]
    pat2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pat3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []

    for idx, ans in enumerate(answers):
        if ans == pat1[idx % len(pat1)]:
            score[0] += 1
        if ans == pat2[idx % len(pat2)]:
            score[1] += 1
        if ans == pat3[idx % len(pat3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx + 1)

    return answer