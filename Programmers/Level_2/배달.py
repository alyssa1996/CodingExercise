from collections import deque
def solution(N, road, K):
    answer = 0
    INF = 1e9
    min_time = [INF] * (N+1)
    min_time[1] = 0
    road_data = [[] for _ in range(N+1)]
    for start, end, time in road:
        road_data[start].append((start, end, time))
        road_data[end].append((end, start, time))
    queue = deque(road_data[1])
    while queue:
        current_village, next_village, time = queue.popleft()
        if min_time[next_village] < min_time[current_village] + time:
            continue
        if min_time[next_village] == INF:
            min_time[next_village] = min_time[current_village] + time
        else:
            min_time[next_village] = min(min_time[next_village], min_time[current_village]+time)
        for village_data in road_data[next_village]:
            queue.append(village_data)

    for time in min_time:
        if time <= K:
            answer += 1
    return answer
