def solution(n):
    listed=[True]*n
    m=int((n**0.5))
    for i in range(2,m+1):
        if listed[i-1]==True:
            for j in range(i+i,n+1,i):
                listed[j-1]=False
    return listed.count(True)-1
