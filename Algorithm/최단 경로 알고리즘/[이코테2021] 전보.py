import sys
import heapq
INF=int(1e9)

n,m,c=map(int,input().split())
graph=[[]for i in range(n+1)]
distance=[INF]*(n+1)

for i in range(m):
    x,y,z=map(int,sys.stdin.readline().split())
    graph[x].append((y,z))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)
time=0
city=n

for i in range(1,n+1):
    if distance[i]==INF:
        city-=1
    else:
        time=max(time,distance[i])

print("%d %d"%(city-1, time))
