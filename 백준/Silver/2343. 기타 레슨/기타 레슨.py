n, m = map(int, input().split())
lectures = list(map(int, input().split()))

def count_blu_ray(lectures, max_size):
    count = 1 # 블루레이 개수, 최소 1개는 필요
    current_sum = 0 # 현재 블루레이에 담긴 강의의 길이 합

    for lecture in lectures:
        if current_sum + lecture <= max_size:
            current_sum += lecture
        else:
            count += 1 # 새로운 블루레이 필요
            current_sum = lecture # 새로운 블루레이에 현재 강의 추가

    return count

def minimum_blu_ray_size(n, m, lectures):
    low, high = max(lectures), sum(lectures)

    while low <= high:
        mid = (low + high) // 2
        if count_blu_ray(lectures, mid) <= m:
            high = mid - 1 # 가능한 크기 중 더 작은 크기 찾기
        else:
            low = mid + 1
    return low


print(minimum_blu_ray_size(n, m, lectures))