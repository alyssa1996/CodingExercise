import heapq
def change_order(heap):
    heap = [-number for number in heap]
    heapq.heapify(heap)
    return heap

def solution(operations):
    answer = []
    heap = []
    for operation in operations:
        if operation[0] == 'I':
            heapq.heappush(heap,int(operation.split()[1]))
        if operation == "D -1" and heap:
            heapq.heappop(heap)
        if operation == "D 1" and heap:
            heap = change_order(heap)
            heapq.heappop(heap)
            heap = change_order(heap)
    
    if heap:
        return [max(heap), min(heap)]
    else:
        return[0,0]
