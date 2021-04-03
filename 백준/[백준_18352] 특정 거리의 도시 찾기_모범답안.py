from collections import deque
import sys

n,m,k,x=map(int,sys.stdin.readline().split())
city=[[] for i in range(n+1)]

for i in range(m):
    start,end=map(int,sys.stdin.readline().split())
    city[start].append(end)

distance=[-1]*(n+1)
distance[x]=0
queue=deque([x])
while queue:
    now=queue.popleft()
    for next_city in city[now]:
        if distance[next_city]==-1:
            distance[next_city]=distance[now]+1
            queue.append(next_city)

check=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True

if check==False:
    print(-1)
