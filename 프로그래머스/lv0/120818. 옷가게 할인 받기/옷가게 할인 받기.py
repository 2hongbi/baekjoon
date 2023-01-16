def solution(price):
    discount = 1
    if price >= 100000:
        discount = 0.95
    if price >= 300000:
        discount = 0.9
    if price >= 500000:
        discount = 0.8
    return (int)(price * discount)