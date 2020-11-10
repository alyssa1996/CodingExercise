def solution(citations):
    answer = 0
    citations.sort()
    for i in range(1,len(citations)+1):
        count=0
        for j in citations:
            if i<=j:
                count+=1
        if i<=count:
            answer=i
    return answer
