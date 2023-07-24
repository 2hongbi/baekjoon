def solution(answers):
    scores = [0, 0, 0]

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for idx, ans in enumerate(answers):
        if ans == student1[idx % len(student1)]:
            scores[0] += 1
        if ans == student2[idx % len(student2)]:
            scores[1] += 1
        if ans == student3[idx % len(student3)]:
            scores[2] += 1
        
    max_score = max(scores)
    answer = [idx + 1 for idx, score in enumerate(scores) if score == max_score] 
    
    
    return answer