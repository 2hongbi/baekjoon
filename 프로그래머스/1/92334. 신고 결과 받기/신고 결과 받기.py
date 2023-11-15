from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    # 한 유저를 여러 번 신고할 수도 있지만, 동일 유저에 대한 신고 횟수는 1회 처리 > set
    report = set(report)
    
    report_dict = defaultdict(list)
    count_dict = defaultdict(int)
    
    for r in report:
        reporter, reported = r.split()
        report_dict[reporter].append(reported)
        count_dict[reported] += 1
        
    for id in id_list:
        result = 0
        for report in report_dict[id]:
            if count_dict[report] >= k:
                result += 1
        
        # 각 유저별로 처리 결과와 메일을 받은 횟수를 배열에 담아 return
        answer.append(result)
        
    return answer
    