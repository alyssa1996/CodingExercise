from collections import deque

n, m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    queue = deque()
    for idx, value in enumerate(indegree):
        if idx == 0:
            continue
        if value == 0:
            queue.append(idx)

    while queue:
        now = queue.popleft()
        result.append(now)
        for idx in graph[now]:
            indegree[idx] -= 1
            if indegree[idx] == 0:
                queue.append(idx)

    return result

print(' '.join(map(str, topology_sort())))
