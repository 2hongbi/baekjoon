def is_hansu(number):
    num_list = list(str(number))

    # 한 자리 수 혹은 두 자리수는 무조건 한수
    if len(num_list) <= 2:
        return True
    else:
        diff = int(num_list[1]) - int(num_list[0])
        for i in range(1, len(num_list) - 1):
            if int(num_list[i + 1]) - int(num_list[i]) != diff:
                # 연속된 두 자릿수의 차이가 일정하지 않으면 한수가 아님
                return False
        return True


def count_hansu(n):
    count = 0
    for number in range(1, n + 1):
        if is_hansu(number):
            count += 1

    return count

N = int(input())
print(count_hansu(N))