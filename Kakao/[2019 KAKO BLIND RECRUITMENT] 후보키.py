from itertools import combinations
def solution(relation):
    row = len(relation)
    col = len(relation[0])
    candidates = []
    for counts in range(1, col+1):
        candidates  += list(combinations(range(col), counts))
    
    unique = []
    for candidate in candidates:
        temp = [tuple([item[idx] for idx in candidate]) for item in relation]
        if len(set(temp)) == row:
            unique.append(candidate)
    
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if unique[i] not in answer or unique[j] not in answer:
                continue
            if set(unique[i])&set(unique[j]) == set(unique[i]):
                answer.remove(unique[j])

    return len(answer)
