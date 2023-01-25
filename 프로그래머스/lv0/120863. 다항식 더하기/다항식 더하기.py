def solution(polynomial):
    x_ans = 0
    int_ans = 0
    for poly in polynomial.split(" + "):
        if 'x' in poly:
            temp = poly.replace('x', '')
            if temp:
                x_ans += int(temp)
            else:
                x_ans += 1
        else:
            int_ans += int(poly)
    ans = ''
    if x_ans > 0:
        if x_ans == 1:
            ans += 'x'
        else:
            ans += str(x_ans) + 'x'
    if int_ans > 0:
        if x_ans > 0:
            ans += ' + ' + str(int_ans)
        else:
            ans += str(int_ans)
    return ans