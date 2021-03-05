import sys
sys.setrecursionlimit(10**9)
def dfs(index):
    #print(tree[index], parent)
    if visited[index]==1:
        return False
    visited[index]=1
    for i in tree[index]:
        if dfs(i):
            parent[i]=index
    return True

n=int(input())
tree=[0]*(n+1)
visited=[0]*(n+1)
parent=[0]*(n+1)

for i in range(n-1):
    x,y=map(int,sys.stdin.readline().split())
    if tree[x]==0:
        tree[x]=[y]
    else:
        tree[x].append(y)
        
    if tree[y]==0:
        tree[y]=[x]
    else:
        tree[y].append(x)

dfs(1)
for i in range(2,n+1):
    print(parent[i])
