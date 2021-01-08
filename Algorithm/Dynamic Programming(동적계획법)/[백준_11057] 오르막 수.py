n=int(input())

d=[[10,9,8,7,6,5,4,3,2,1]]
for i in range(1,n):
    d.append([sum(d[i-1])])
    for j in range(10):
        d[i].append(d[i][j]-d[i-1][j])

print(d[n-1][0]%10007)
