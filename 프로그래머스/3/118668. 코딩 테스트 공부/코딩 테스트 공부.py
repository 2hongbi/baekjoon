def solution(alp, cop, problems):
    # 모든 문제를 풀기 위해 필요한 최대 알고력과 코딩력을 구한다
    max_alp = max([alp] + [p[0] for p in problems])
    max_cop = max([cop] + [p[1] for p in problems])

    # dp 테이블 초기화 (최대 알고력과 코딩력까지 고려)
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    # 각 알고력, 코딩력 조합에 대해 최소 시간 계산
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 현재 알고력, 코딩력에서 1 증가하는 경우의 시간 계산
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            # 각 문제를 푸는 경우의 시간 계산
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp = min(max_alp, i + alp_rwd)
                    next_cop = min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

    return dp[max_alp][max_cop]