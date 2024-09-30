def find_keyword(s, k):
    filtered_s = ''.join([char for char in s if not char.isdigit()])

    if k in filtered_s:
        return 1
    else:
        return 0

s = input().strip()
k = input().strip()
print(find_keyword(s, k))