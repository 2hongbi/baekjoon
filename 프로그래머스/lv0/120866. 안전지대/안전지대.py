def solution(board):
    answer = len(board) * len(board[0])

    safe = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    def is_in_board(row, col):
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 1:
                for dr in range(-1, 2):
                    nr = r + dr
                    for dc in range(-1, 2):
                        # 지뢰 주변의 구역 + 지뢰 구역에 대한 위치
                        nc = c + dc

                        if is_in_board(nr, nc):
                            # 위험지역 카운트(최초 전체를 안전지역이라고 가정했으므로 1씩 빼기)
                            # xor 연산 이용
                            # 1. safe[nr][nc]가 1인 경우(이전에 위험지역으로 설정한 경우) 뺄 필요 없음
                            #    따라서 1 -> 0으로 계산
                            # 2. safe[nr][nc]가 0인 경우(이전에 위험지역으로 설정하지 않은 경우) 위험지역 카운트
                            #    따라서 0 -> 1로 계산
                            answer -= safe[nr][nc] ^ 1
                            # or 연산으로 위험지역 설정(safe[nr][nc]가 기존에 1이든 0이든 값은 1)
                            safe[nr][nc] |= 1

    return answer