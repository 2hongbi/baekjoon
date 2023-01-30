def solution(score):
    dict, avg_list = {}, [sum(s) / 2 for s in score]
    print(avg_list)
    for idx, avg in enumerate(sorted(avg_list, reverse=True), start=1):
        if avg not in dict:
            dict[avg] = idx
    print(dict)
    return [dict[avg] for avg in avg_list]