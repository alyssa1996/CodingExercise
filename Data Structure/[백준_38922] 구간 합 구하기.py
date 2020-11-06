n,m,k=input("").split(" ")

numbers=list()
for i in range(int(n)):
    numbers.append(int(input("")))

for i in range(int(m)+int(k)):
    order=input("").split(" ")
    if order[0]=='1':
        numbers[int(order[1])-1]=int(order[2])
    elif order[0]=='2':
        print(sum(numbers[int(order[1])-1:int(order[2])]))
