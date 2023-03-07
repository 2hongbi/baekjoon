from itertools import product

def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    for i in range(1, 6):
        for comb in product(vowel, repeat=i):
            words.append(''.join(list(comb)))
    
    words.sort()
    return words.index(word) + 1