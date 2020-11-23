

n=int(input())

numbers=list()
for i in range(n):
    num=int(input())
    index=len(numbers)-1
    while index>-1 and numbers[index]>num:
        index-=1
    numbers.insert(index+1,num)
    
for i in numbers:
    print(i)
