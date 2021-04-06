city=int(input())
road=list(map(int,input().split()))
oil_cost=list(map(int,input().split()))

index=1
min_oil=0
total=0
while True:
    if index==city-1:
        break
    if oil_cost[min_oil]<=oil_cost[index]:
        index+=1
    else:
        total+=(oil_cost[min_oil]*sum(road[min_oil:index]))
        min_oil=index
        index+=1
        
total+=(oil_cost[min_oil]*sum(road[min_oil:]))
print(total)
