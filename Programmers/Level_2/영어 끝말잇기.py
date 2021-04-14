def solution(n, words):
    answer = [0,0]
    members=[[] for i in range(n)]
    members[0].append(words[0])
    index=1
    for i in range(1,len(words)):
        if index==n:
            index=0
        if words[i][0] != words[i-1][-1]:
            answer=[index+1,len(members[index])+1]
            break
        check=True
        for j in range(len(members)):
            if words[i] in members[j]:
                answer=[index+1,len(members[index])+1]
                check=False
                break
        if not check:
            break
        else:
            members[index].append(words[i])
            index+=1
    return answer
