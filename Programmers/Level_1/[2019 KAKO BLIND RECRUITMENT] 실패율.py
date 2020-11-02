def solution(N, stages):
    answer = []
    stages.sort()
    fail=list()
    index=list()
    for i in range(N):
        if i+1 in stages:
            fail.append(stages.count(i+1)/len(stages[stages.index(i+1):]))
        elif i+1 <max(stages):
            fail.append(0/stages.count(max(stages)))
        else:
            fail.append(0)
        index.append(i+1)
        
    while len(fail)>0:
        location=fail.index(max(fail))
        answer.append(index[location])
        index.pop(location)
        fail.pop(location)
    
    return answer
