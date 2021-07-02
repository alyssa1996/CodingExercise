def find_parent(parents, island):
    if parents[island] != island:
        parents[island] = find_parent(parents, parents[island])
    return parents[island]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, costs):
    answer = 0
    parents = [i for i in range(n+1)]
    islands = [(cost, ia, ib) for ia, ib, cost in costs]
    islands.sort()
    
    for connection in islands:
        cost, ia, ib = connection
        if find_parent(parents, ia) != find_parent(parents, ib):
            union_parent(parents, ia, ib)
            answer += cost
    return answer
