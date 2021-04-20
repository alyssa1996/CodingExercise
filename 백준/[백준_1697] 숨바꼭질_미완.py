from collections import deque

n, k = map(int, input().split())
if n == k:
    print(0)
else:
    visited = {}
    queue = deque([n])
    sec=0
    while queue:
        temp_queue=deque()
        for value in queue:
            temp_queue.append(value)
        queue.clear()
        sec+=1
        check=False

        while temp_queue:
            current = temp_queue.popleft()
            if current == k:
                break

            if current in visited:
                continue

            visited[current]=True
            if current+1 == k or current-1 == k or 2*current == k:
                check = True
                break

            queue.append(current-1)
            queue.append(current+1)
            queue.append(2*current)

        if check:
            break

    print(sec)
