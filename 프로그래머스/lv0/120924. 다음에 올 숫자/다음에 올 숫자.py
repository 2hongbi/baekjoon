def solution(common):
    seq = [y - x for x, y in zip(common, common[1:])]
    
    if len(set(seq)) == 1:
        return common[0] + seq[0] * len(common)
    else:
        gongbi = seq[1] // seq[0]
        return common[0] * (gongbi ** len(common))