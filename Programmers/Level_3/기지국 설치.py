import math
def solution(n, stations, w):
    answer = 0
    
    area = []
    if stations[0] - w - 1 >= 1:
        area.append([1, stations[0]-w-1])
    
    if stations[-1]+w+1 <= n:
        area.append([stations[-1]+w+1, n])
    
    for idx in range(len(stations)-1):
        start = stations[idx] + w + 1
        end = stations[idx+1] - w - 1
        if start <= end:
            area.append([start, end])

    length = []
    for start, end in area:
        length.append(end - start + 1)
    
    for candidate in length:
        answer += math.ceil(candidate/(2*w+1))

    return answer
