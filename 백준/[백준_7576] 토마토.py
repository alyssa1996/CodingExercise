import sys
from collections import deque
input=sys.stdin.readline
m,n=map(int,input().split())
tomato=[]
count=0
for i in range(n):
    tomato.append(list(map(int,input().split())))
    count+=tomato[-1].count(0)

dx=[0,0,-1,1]
dy=[-1,1,0,0]
tomato_location=deque([])
visited=[[False]*m for i in range(n)]

def extend(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if tomato[nx][ny]==0:
                tomato[nx][ny]=1
                tomato_location.append((nx,ny))

def bfs():
    day=0
    while tomato_location:
        now=len(tomato_location)
        for i in range(now):
            x,y=tomato_location.popleft()
            if visited[x][y]:
                continue
            visited[x][y]=True
            extend(x,y)
        day+=1
    return day

if count==0:
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if tomato[i][j]==1:
                tomato_location.append((i,j))
                
    count=bfs()        
    check=True
    for i in range(n):
        if 0 in tomato[i]:
            check=False
            break
        
    if check:
        print(count-1)
    else:
        print(-1)
        

    
