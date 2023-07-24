from itertools import product

def solution(word):
    words = []
    
    for i in range(1, 6):
        for comb in product('AEIOU', repeat=i):
            words.append(''.join(list(comb)))
    
    words.sort()
    return words.index(word) + 1