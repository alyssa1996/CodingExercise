import heapq
n=int(input())
heap=[]
for i in range(n):
    number=int(input())
    heapq.heappush(heap,number)
    print(heap)
    length=len(heap)
    if length%2==0:
        print(min(heap[length//2-1],heap[length//2]))
    else:
        print(heap[length//2])
