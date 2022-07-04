num_list = list(map(int, input().split()))
sum_value = sum(i ** 2 for i in num_list)
print(sum_value % 10)