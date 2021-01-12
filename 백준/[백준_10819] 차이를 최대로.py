n=int(input())
li=list(map(int,input().split()))

sort=sorted(li)
result=list()

for i in range(len(li)//2):
    if i%2==0:
        result.insert(0,sort.pop(0))
        result.append(sort.pop())
    else:
        result.insert(0,sort.pop())
        result.append(sort.pop(0))

if len(sort):
    if abs(sort[0]-result[0])<abs(sort[0]-result[len(result)-1]):
        result.append(sort[0])
    else:
        result.insert(0,sort[0])
    
answer=0
for i in range(1,len(result)):
    answer+=abs(result[i-1]-result[i])

print(answer)
