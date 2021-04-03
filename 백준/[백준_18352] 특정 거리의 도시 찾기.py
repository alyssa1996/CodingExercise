#시간초과 발생

from collections import deque
import sys

n,m,k,x=map(int,sys.stdin.readline().split())
distance=[0]*(n+1)
visited=[False]*(n+1)
city=[[] for i in range(n+1)]

for i in range(m):
    start,end=map(int,sys.stdin.readline().split())
    city[start].append((end,start))

queue=deque(city[x])
visited[x]=True

while queue:
    current_city=queue.popleft()
    now=current_city[0]
    previous=current_city[1]
    if visited[now]:
        continue

    if distance[now]:
        distance[now]=min(distance[now],distance[previous]+1)
    else:
        distance[now]=distance[previous]+1
    visited[now]=True

    for i in range(len(city[now])):
        if city[now][i] not in queue:
            queue.append(city[now][i])

result=[]
for i in range(len(distance)):
    if distance[i]==k:
        result.append(i)

if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)
