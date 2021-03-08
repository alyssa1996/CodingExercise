def solution(N,stages):
    users=[0]*(N+2)
    answer=[0]*(N+1)
    
    for i in stages:
        users[i]+=1

    for i in range(1,len(users)-1):
        if sum(users[i:])==0:
            answer[i]=(i,0)
        else:
            answer[i]=(i,users[i]/sum(users[i:]))

    del answer[0]
    answer.sort(reverse=True,key=lambda x:x[1])
    
    result=[]
    for i in answer:
        result.append(i[0])

    return result

print(solution(4,[4,4,4,4,4]))


    
