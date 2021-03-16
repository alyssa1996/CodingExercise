n=int(input())
ar=list(map(int,input().split()))
array=ar.copy()
if ar[1]<ar[0]:
    ar[1]=ar[0]

for i in range(2,len(ar)):
    ar[i]=max(ar[i-1],ar[i-2]+ar[i])

print(max(ar))

#모범답안
d=[0]*100

d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])

print(d[n-1])
