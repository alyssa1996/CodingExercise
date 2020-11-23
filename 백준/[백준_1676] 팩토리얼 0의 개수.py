num=int(input())

fact=1
for i in range(2,num+1):
    fact*=i

fact=str(fact)
count=0
for i in fact[::-1]:
    if i=='0':
        count+=1
    else:
        break
print(count)
