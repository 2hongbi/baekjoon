num_list = []
for i in range(9):
    num_list.append(int(input()))
max_val = max(num_list)
idx = num_list.index(max_val) + 1
print(max_val)
print(idx)