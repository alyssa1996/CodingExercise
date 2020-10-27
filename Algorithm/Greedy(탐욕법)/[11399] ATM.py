#백준 https://www.acmicpc.net/problem/11399

people=int(input(""))
order=input("").split(" ")

for i in range(len(order)):
    order[i]=int(order[i])

order=sorted(order)

total=0
for i in range(len(order)):
    total+=sum(order[:i+1])

print(total)
