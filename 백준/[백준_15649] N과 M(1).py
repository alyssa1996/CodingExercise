def dfs(ar,n,m):
    if len(ar)==m:
        print(' '.join(map(str,ar)))
        return
    for i in range(1,n+1):
        if i in ar:
            continue
        ar.append(i)
        dfs(ar,n,m)
        ar.pop()

n,m=map(int,input().split())
dfs([],n,m)
