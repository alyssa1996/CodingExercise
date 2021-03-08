import sys
import heapq
n=int(input())
cards=[]

for i in range(n):
    heapq.heappush(cards,int(sys.stdin.readline()))

result=0
while True:
    if len(cards)<=1:
        break
    temp=heapq.heappop(cards)+heapq.heappop(cards)
    result+=temp
    heapq.heappush(cards,temp)
    
print(result)
