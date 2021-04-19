import sys
from collections import deque

def dfs(nodes,v,visited,result):
    if visited[v]:
        return
    visited[v]=True
    result.append(v)
    for n_node in nodes[v]:
        dfs(nodes,n_node,visited,result)

    return ' '.join(map(str,result))

def bfs(nodes,v):
    visited=[False for _ in range(n+1)]
    queue=deque()
    queue.append(v)
    result=[]
    while queue:
        c_node=queue.popleft()
        if visited[c_node]:
            continue
        visited[c_node]=True
        result.append(c_node)
        for n_node in nodes[c_node]:
            queue.append(n_node)
    return ' '.join(map(str,result))


input=sys.stdin.readline
n,m,v=map(int,input().split())
nodes=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
queue=[]

for _ in range(m):
    node1,node2=map(int,input().split())
    nodes[node1].append(node2)
    nodes[node2].append(node1)

for idx,value in enumerate(nodes):
    value.sort()

print(dfs(nodes,v,visited,[]))
print(bfs(nodes,v))
    
