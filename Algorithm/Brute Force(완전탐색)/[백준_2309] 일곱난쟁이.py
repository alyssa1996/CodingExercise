n=[0]*9

for i in range(9):
    n[i]=int(input())

n.sort()
total=sum(n)
for i in range(8,-1,-1):
    check=False
    for j in range(i-1,-1,-1):
        if total-n[i]-n[j]==100:
            check=True
            n[i]=0
            n[j]=0
            break
    if check:
        break

for i in range(9):
    if n[i]:
        print(n[i])
