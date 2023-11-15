def solution(n, info):
    max_diff = -1
    answer = [-1]

    def backtrack(ryan_scores, idx, arrows_left):
        nonlocal max_diff, answer
        # 화살을 다 쏜 경우 또는 모든 점수를 확인한 경우
        if arrows_left == 0 or idx == 11:
            ryan_total, apeach_total = 0, 0
            for i in range(11):
                if ryan_scores[i] > info[i]:
                    ryan_total += 10 - i
                elif info[i] > 0:
                    apeach_total += 10 - i
            diff = ryan_total - apeach_total
            # 라이언이 우승할 수 있는 경우
            if diff > 0 and diff >= max_diff:
                # 동일한 점수 차이일 때 더 낮은 점수에 많은 화살을 쏜 경우를 선택
                if diff > max_diff or ryan_scores[::-1] > answer[::-1]:
                    max_diff = diff
                    answer = ryan_scores.copy()
            return

        # 현재 점수(idx)에서 어피치보다 1발 더 쏘거나 쏘지 않는 경우 탐색
        if arrows_left > info[idx]:
            ryan_scores[idx] = info[idx] + 1
            backtrack(ryan_scores, idx + 1, arrows_left - info[idx] - 1)
        ryan_scores[idx] = 0
        backtrack(ryan_scores, idx + 1, arrows_left)

    backtrack([0] * 11, 0, n)
    # 모든 화살을 쏘지 않은 경우 마지막에 남은 화살을 0점에 할당
    if answer[-1] != -1:
        answer[-1] += n - sum(answer)
    return answer