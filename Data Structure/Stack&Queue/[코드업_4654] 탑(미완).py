number=int(input(""))
tops=input("").split()

result=[0]*number
print(tops)
for i in range(number):
    current=int(tops.pop())
    index=len(tops)-1
    while index>=0:
        if current<int(tops[index]):
            result[number-1-i]=index+1
            break
        else:
            index-=1

for i in result:
    print(i, end=" ")
