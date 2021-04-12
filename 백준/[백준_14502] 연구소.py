import sys
input=sys.stdin.readline
n,m=map(int,input().split())
lab=[]
temp=[[0] for _ in range(n)]
for i in range(n):
    lab.append(list(map(int,input().split())))

max_safe=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def count_safe():
    result=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                result+=1
    return result

def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)


def dfs(wall,x,y):
    global max_safe

    if wall==3:
        for i in range(n):
            temp[i]=lab[i][:]

        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
                    
        max_safe=max(max_safe,count_safe())
        return

    for i in range(x,n):
        for j in range(y,m):
            if lab[i][j]==0:
                lab[i][j]=1
                wall+=1
                dfs(wall,i,j+1)
                lab[i][j]=0
                wall-=1
        y=0
    
dfs(0,0,0)
print(max_safe)
