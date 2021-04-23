def solution(absolutes, signs):
    answer = 0
    for idx, value in enumerate(absolutes):
        if signs[idx]:
            answer += value
        else:
            answer += -value
    return answer
