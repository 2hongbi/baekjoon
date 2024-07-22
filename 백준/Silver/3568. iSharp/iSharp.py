# https://www.acmicpc.net/problem/3568

statements = input().replace(';', '').split()

base_type = statements.pop(0)

for stmt in statements:
    stmt = stmt.replace(',', '')

    temp_var, temp_type = '', '' # 변수 이름, 추가 타입

    idx = 0
    while idx < len(stmt):
        if stmt[idx].isalpha():
            temp_var += stmt[idx] # 알파벳은 변수명에 추가
        else:
            if stmt[idx] == '[' and idx + 1 < len(stmt) and stmt[idx + 1] == ']':
                temp_type += ']['
                idx += 1
            else: # [] 이외 처리
                temp_type += stmt[idx]
        idx += 1

    print(base_type + temp_type[::-1] + ' ' + temp_var + ';')