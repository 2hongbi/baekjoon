def solution(spell, dic):
    spell = set(spell)
    for d in dic:
        if spell.issubset(d):
            return 1
    return 2