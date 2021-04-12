def solution(s):
    s=s[1:-1].split(',')
    result=[]
    for i in range(len(s)):
        current=s[i].strip("{}")
        result.append(int(current))
    
    set_result=list(set(result))
    answer = [0]*len(set_result)
    
    for i in range(len(set_result)):
        answer[result.count(set_result[i])-1]=set_result[i]
    answer.reverse()
    
    return answer
