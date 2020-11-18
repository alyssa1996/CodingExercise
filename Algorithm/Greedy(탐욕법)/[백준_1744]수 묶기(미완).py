#음수양수 나눠서 계산해야함

n=int(input())
number=list()
for i in range(n):
    number.append(int(input()))

number.sort(reverse=True)
index=0
total=0
while index<n:
    print(index, number[index],total)
    if index==n-1:
        total+=number[index]
        break
    multiply= number[index]*number[index+1]
    if  multiply > number[index]:
        total+=number[index]*number[index+1]
        index+=2
    elif multiply == number[index] and number[index]==0:
        total+=number[index]*number[index+1]
        index+=2
    elif multiply<=number[index]:
        total+=number[index]
        index+=1
    
print(total)
