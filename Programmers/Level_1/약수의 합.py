def solution(n):
    answer = 0
    if n in (0,1):
        answer=n
        return answer
    
    for i in range(2,n):
        if n%i==0:
            answer+=i
    answer=answer+1+n
    return answer
