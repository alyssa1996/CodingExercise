rest=[0]*42

for i in range(10):
    num=int(input())
    rest[num%42]+=1

count=0
for i in rest:
    if i:
        count+=1
print(count)
