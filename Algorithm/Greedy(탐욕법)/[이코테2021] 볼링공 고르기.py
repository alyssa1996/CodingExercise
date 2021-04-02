from itertools import combinations

n,m=map(int,input().split())
balls=list(map(int,input().split()))
result=list(combinations(balls,2))
total=len(result)

for i in result:
    if i[0]==i[1]:
        total-=1

print(total)
