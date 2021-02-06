from sys import stdin
n=int(stdin.readline())

locations=[0]*n
for i in range(n):
    temp=list(map(int,stdin.readline().split()))
    locations[i]=[temp[1],temp[0]]

locations.sort()
for i in range(n):
    print(locations[i][1],locations[i][0])
