#백준 https://www.acmicpc.net/problem/11047

num,total=input("").split(" ")
num, total=int(num), int(total)

coins=list()
for i in range(num):
    coins.append(int(input("")))

count=0
for i in range(len(coins)-1,-1,-1):
    if total//coins[i]>0:
        count+=total//coins[i]
        total=total%coins[i]
print(count)
