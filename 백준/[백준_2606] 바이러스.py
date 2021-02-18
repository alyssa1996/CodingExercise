def DFS(this):
    if visited[this]:
        return
    visited[this]=1
    for i in computers[this]:
        DFS(i-1)

n=int(input())
computers=[]
visited=[0]*n

for i in range(n):
    computers.append([])

m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    computers[a-1].append(b)
    computers[b-1].append(a)

DFS(0)
print(visited.count(1)-1)


