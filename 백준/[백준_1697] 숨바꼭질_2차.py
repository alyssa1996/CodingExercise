from collections import deque
n, k = map(int, input().split())

def bfs():
    queue = deque([])
    queue.append(n+1)
    queue.append(n-1)
    queue.append(n*2)

    answer = 0
    visited = set()

    while queue:
        current_length = len(queue)
        answer += 1
        is_found = False
        for _ in range(current_length):
            current_location = queue.popleft()
            if current_location == k:
                is_found = True
                break
            if current_location in visited:
                continue
            visited.add(current_location)
            if 0 <= current_location+1 <= 100_000:
                queue.append(current_location+1)
            if 0 <= current_location-1 <= 100_000:
                queue.append(current_location-1)
            if 0 <= current_location*2 <= 100_000:
                queue.append(current_location*2)
        if is_found:
            break
        
    return answer

if n==k:
    print(0)
else:
    print(bfs())

