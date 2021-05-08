from collections import defaultdict
def solution(gems):
    answer = []
    start, end = 0, 0
    all_gems = len(set(gems))
    current_gems = defaultdict(int)
    min_interval = 100000
    while end < len(gems):
        current_gems[gems[end]] += 1
        end += 1
        if len(current_gems) == all_gems:
            while start < end:
                if current_gems[gems[start]] > 1:
                    current_gems[gems[start]] -= 1
                    start += 1
                elif end - start < min_interval:
                    min_interval = end - start 
                    answer = [start+1, end]
                    break
                else: 
                    break
    return answer
