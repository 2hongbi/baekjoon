import re

def search(idx, visit, user_id, answer, ban_patterns):
    if idx == len(ban_patterns):
        answer.append(visit)
        return
    
    for i in range(len(user_id)):
        if (visit & (1 << i)) > 0 or not re.fullmatch(ban_patterns[idx], user_id[i]):
            continue
        search(idx + 1, visit | (1 << i), user_id, answer, ban_patterns)

        
def solution(user_id, banned_id):
    answer = []
    ban_patterns = [x.replace('*', '.') for x in banned_id]
    search(0, 0, user_id, answer, ban_patterns)
    return len(set(answer))