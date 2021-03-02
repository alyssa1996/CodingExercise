position=input()

column=['a','b','c','d','e','f','g','h']
board=[]
for i in range(8):
    board.append([])
    for j in range(8):
        board[-1].append((i,j))

x,y=column.index(position[0]),int(position[1])-1
dx=[-2,-2,-1,-1,1,1,2,2]
dy=[-1,1,-2,2,-2,2,-1,1]
count=0
for i in range(len(dx)):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or ny<0 or nx>=8 or ny>=8:
        continue
    print(nx,ny)
    count+=1

print(count)
