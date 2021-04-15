from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache=deque([])
    if cacheSize==0:
        return len(cities)*5
    for i in range(len(cities)):
        current=cities[i].lower()
        if current in cache:
            cache.remove(current)
            answer+=1
        elif len(cache)==cacheSize:
            cache.popleft()
            answer+=5
        else:
            answer+=5
        cache.append(current)
    return answer
