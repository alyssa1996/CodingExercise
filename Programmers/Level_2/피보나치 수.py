def solution(n):
    answer=0
    start=0
    end=1
    for i in range(2,n+1):
        answer=start+end
        start=end
        end=answer
    return answer%1234567
