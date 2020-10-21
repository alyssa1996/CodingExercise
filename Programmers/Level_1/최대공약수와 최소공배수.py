def solution(n, m):
    if n>m:
        n,m=m,n
    answer = []
    
    for i in range(n+1,0,-1):
        if n%i==0 and m%i==0:
            answer.append(i)
            break
    for i in range(m, (n*m)+1):
        if i%m==0 and i%n==0:
            answer.append(i)
            break
    return answer
