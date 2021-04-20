from collections import deque
airports = {}

def dfs():
    stack = ["ICN"]
    path = []
    while stack:
        start = stack[-1]
        if start not in airports or len(airports[start]) == 0:
            path.append(stack.pop())
        else:
            stack.append(airports[start].popleft())
    
    return path[::-1]
    

def solution(tickets):
    for idx,value in enumerate(tickets):
        if value[0] in airports:
            airports[value[0]].append(value[1])
        else:
            airports[value[0]]=[value[1]]
    
    
    for key,value in airports.items():
        value.sort()
        airports[key]=deque(value)
    
    return dfs()
