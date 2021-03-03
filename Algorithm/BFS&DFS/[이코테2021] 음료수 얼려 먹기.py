n,m=map(int,input().split())

def bfs(ice,i,j):
    ice[i][j]='1'
    if j+1>=m and i+1>=n:
        return
    elif j+1>=m and ice[i+1][j]=='1':
        return
    elif i+1>=n and ice[i][j+1]=='1':
        return
    elif ice[i][j+1]=='1' and ice[i+1][j]=='1':
        return

    stack=[]
    if ice[i][j+1]=='0':
        stack.append((i,j+1))
    if ice[i+1][j]=='0':
        stack.append((i+1,j))

    for k in stack:
        bfs(ice,k[0],k[1])

#모범답안
def dfs(x,y):
    if x<= -1 or x>=n or y<=-1 or y>=m:
        return False

    if ice[x][y]==0:
        ice[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


ice=[]
for i in range(n):
    #ice.append(list(input()))
    ice.append(list(map(int,input())))

count=0
for i in range(n):
    for j in range(m):
        '''
        if ice[i][j]=='1':
            continue
        count+=1
        bfs(ice,i,j)
        '''
        if dfs(i,j)==True:
            count+=1


print(count)
