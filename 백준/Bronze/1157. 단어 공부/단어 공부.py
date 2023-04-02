s = input().upper()

cnt_list = list(set(s))
count_list = []
for i in cnt_list:
    cnt = s.count(i)
    count_list.append(cnt)

print('?' if count_list.count(max(count_list)) > 1 else cnt_list[count_list.index(max(count_list))])