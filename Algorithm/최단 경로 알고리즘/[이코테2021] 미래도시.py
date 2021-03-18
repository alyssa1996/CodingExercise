import sys
n,m=map(int,input().split())
INF=int(1e9)
graph=[[INF]*(n+1) for i in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=1
    graph[b][a]=1

x,k=map(int,input().split())
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])

if graph[1][k]==INF or graph[k][x]==INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])
