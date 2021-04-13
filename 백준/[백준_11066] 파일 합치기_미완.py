import heapq
import sys
input=sys.stdin.readline

def get_cost(heap):
    cost=0
    while heap:
        if len(heap)==1:
            break
        x=heapq.heappop(heap)
        y=heapq.heappop(heap)
        cost+=(x+y)
        heapq.heappush(heap,x+y)
        print(heap, cost)
        
    return cost

for i in range(int(input())):
    k=int(input())
    file=list(map(int,input().split()))
    heap=[]
    for j in range(k):
        heapq.heappush(heap,file[j])

    print(get_cost(heap))
    
