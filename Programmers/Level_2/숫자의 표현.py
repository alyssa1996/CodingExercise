def solution(n):
    answer = 0
    for i in range(n+1):
        total=0
        for j in range(i+1,n+1):
            total+=j
            if total==n:
                answer+=1
                break
            elif total>n:
                break
    return answer
