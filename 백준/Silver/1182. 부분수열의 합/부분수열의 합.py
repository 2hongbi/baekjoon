import sys

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0


def back_tracking(idx, res):
    global cnt  # 전역 변수 수정하고 싶을 때
    if idx >= N:
        return
    res += nums[idx]
    # 현재 수열이 S와 같다면 count++
    if res == S:
        cnt += 1

    back_tracking(idx+1, res)  # 이번 숫자 포함 O
    back_tracking(idx+1, res - nums[idx])  # 이번 숫자 포함 X -> 해당 원소가 가리키는 값 제외


back_tracking(0, 0)
print(cnt)