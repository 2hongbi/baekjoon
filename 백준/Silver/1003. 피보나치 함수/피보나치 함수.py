def fibonacci_count(n):
    dp_zero = [0] * (n + 1)
    dp_one = [0] * (n + 1)

    # initialize
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1

    dp_zero[0], dp_one[0] = 1, 0  # fibonacci(0)
    dp_zero[1], dp_one[1] = 0, 1  # fibonacci(1)

    for i in range(2, n + 1):
        dp_zero[i] = dp_zero[i - 1] + dp_zero[i - 2]
        dp_one[i] = dp_one[i - 1] + dp_one[i - 2]

    return dp_zero[n], dp_one[n]


t = int(input())
for _ in range(t):
    zero_count, one_count = fibonacci_count(int(input()))
    print(zero_count, one_count)