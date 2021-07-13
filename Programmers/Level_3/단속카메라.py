def solution(routes):
    answer = 1
    routes.sort(reverse=True)
    current = routes[0][0]
    for idx in range(1, len(routes)):
        if routes[idx][1] < current:
            answer += 1
            current = routes[idx][0]
    return answer
