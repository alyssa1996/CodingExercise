import sys
sys.setrecursionlimit(100000)

def dfs(array,n,m):
    if len(array)==m:
        print(' '.join(map(str,array)))
        return
    for i in range(1,n+1):
        array.append(i)
        dfs(array,n,m)
        array.pop()

n,m=map(int,input().split())
dfs([],n,m)
