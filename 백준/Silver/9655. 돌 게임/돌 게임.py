def find_winner(n):
    if n % 2 == 0:
        return 'CY'
    return 'SK'

n = int(input())
print(find_winner(n))