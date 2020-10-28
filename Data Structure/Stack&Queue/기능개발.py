# 프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    finished=list()
    answer = []
    
    for i in range(len(progresses)):
        remain=100-progresses[i]
        if remain%speeds[i]==0:
            day=remain//speeds[i]
        else:
            day=remain//speeds[i]+1
        finished.append(day)
    
    next=0
    for i in range(len(finished)):
        if next<finished[i]:
            answer.append(1)
            next=finished[i]
        else:
            answer[len(answer)-1]+=1
            
    return answer
