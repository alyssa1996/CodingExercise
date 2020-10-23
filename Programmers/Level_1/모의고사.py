#https://programmers.co.kr/learn/courses/30/lessons/42840
#완전탐색

def getScore(answers,student):
    std=0
    score=0
    for i in answers:
        if std == len(student):
            std=0
        if student[std]==i:
            score+=1
        std+=1
    return score

def solution(answers):
    answer = []
    student=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    score=list()
    for i in range(3):
        score.append(getScore(answers,student[i]))
    
    for index, result in enumerate(score):
        if result == max(score):
            answer.append(index+1)
    
    return sorted(answer)
