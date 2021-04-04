import sys
from itertools import permutations

def caculations(num1,num2,op):
    if op==1:
        return num1+num2
    if op==2:
        return num1-num2
    if op==3:
        return num1*num2
    if op==4:
        if num1<0:
            return -((-num1)//num2)
        else:
            return num1//num2

n=int(input())
numbers=list(map(int,sys.stdin.readline().split()))
operator=list(map(int,sys.stdin.readline().split()))

# +=>1 / -=>2 / *=>3 / //=>4
data=[]
for i in range(len(operator)):
    if operator[i]>=1:
        for j in range(operator[i]):
            data.append(i+1)

if len(data)==1:
    result=caculations(numbers[0],numbers[1],data[0])
    print(result)
    print(result)
else:
    operations=list(set(permutations(data,len(data))))
    result=[]
    for oper in operations:
        current=numbers[0]
        for i in range(len(oper)):
            current=caculations(current,numbers[i+1],oper[i])
        result.append(current)
    result=set(result)
    print(max(result))
    print(min(result))
