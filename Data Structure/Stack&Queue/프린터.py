#프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    while True:
        if priorities[0]==max(priorities):
            answer+=1
            if location==0:
                break
            priorities.pop(0)
            location-=1
        else:
            if location==0:
                location=len(priorities)-1
            else:
                location-=1
            priorities.append(priorities.pop(0))
    return answer
