n, m = map(int, input().split()) # 듣도 못한 사람 수, 보도 못한 사람 수
n_list = [input().strip() for _ in range(n)]
m_list = [input().strip() for _ in range(m)]

result = list(set(n_list) & set(m_list))

print(len(result))
for r in sorted(result):
    print(r)