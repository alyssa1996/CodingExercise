n=int(input())
plan=input().split()
travel_map=[]
for i in range(n):
    travel_map.append([])
    for j in range(n):
        travel_map[-1].append((i,j))

x,y=0,0
for i in plan:
    if i=='L':
       nx,ny=x,y-1
    elif i=='R':
        nx,ny=x,y+1
    elif i=='U':
        nx,ny=x-1,y
    elif i=='D':
        nx,ny=x+1,y
        
    if nx<0 or ny<0 or nx>=n or ny>=n:
        continue
    x,y=nx,ny

print(x+1,y+1)
