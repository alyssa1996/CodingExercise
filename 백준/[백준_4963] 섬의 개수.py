import sys
sys.setrecursionlimit(2500)

def dfs(x,y):
    if x>=h or x<0 or y>=w or y<0:
        return False

    if graph[x][y]==1:
        graph[x][y]=0
        for i in range(8):
            dfs(x+dx[i],y+dy[i])
        return True
    return False

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    
    graph=[]
    count=0
    dx=[-1,1,0,0,-1,-1,1,1]
    dy=[0,0,-1,1,-1,1,-1,1]
    for i in range(h):
        graph.append(list(map(int,input().split())))

    for i in range(h):
        for j in range(w):
            if dfs(i,j)==True:
                count+=1
    print(count)
