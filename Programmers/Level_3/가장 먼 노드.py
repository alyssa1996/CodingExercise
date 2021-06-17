from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    depth = [0 for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    queue = deque(graph[1])
    visited[0] = True
    visited[1] = True
    while queue:
        current_queue = len(queue)
        for node, visit in enumerate(visited):
            if not visit:
                depth[node] += 1
        for _ in range(current_queue):
            next_node = queue.popleft()
            if visited[next_node]:
                continue
            visited[next_node] = True
            for node in graph[next_node]:
                queue.append(node)
    return depth.count(max(depth))
