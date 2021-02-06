n=int(input())

locations=list()
for i in range(n):
    locations.append(list(map(int,input().split())))

locations.sort(key=lambda x:x[1])
for i in range(n):
    print(locations[i][0],locations[i][1])
