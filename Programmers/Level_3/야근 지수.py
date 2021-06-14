import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-work for work in works]
    heapq.heapify(works)
    
    for _ in range(n):
        current = heapq.heappop(works)+1
        if current:
            heapq.heappush(works, current)
    
    return sum([work**2 for work in works])
