from collections import deque

def relationship(target):
    print("current :", target)
    
    if target==y:
        return True
    if visited[target]==1:
        return False
    
    visited[target]=1
    for i in family[target]:
        check=relationship(i)
        if :
            break

n=int(input())
visited=[0]*(n+1)
family=[0]*(n+1)
x,y=map(int,input().split())

m=int(input())
for i in range(m):
    parent,child=map(int,input().split())
    if family[parent]==0:
        family[parent]=[child]
    else:
        family[parent].append(child)
    if family[child]==0:
        family[child]=[parent]
    else:
        family[child].append(parent)

relationship(x)
print(sum(visited))

    
