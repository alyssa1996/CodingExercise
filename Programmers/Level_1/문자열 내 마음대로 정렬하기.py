def solution(strings, n):
    answer = []
    strings_sorted=sorted(strings)
    index=sorted([i[n] for i in strings])
    
    for i in index:
        for j in strings_sorted:
            if i==j[n]:
                answer.append(j)
                strings_sorted.pop(strings_sorted.index(j))
                break
    
    return answer

