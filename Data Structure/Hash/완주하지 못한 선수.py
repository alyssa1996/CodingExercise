def solution(participant, completion):
    sorted_participant=sorted(participant)
    sorted_completion=sorted(completion)
    for i in range(len(completion)):
        if sorted_participant[i]==sorted_completion[i]:
            continue
        else:
            answer=sorted_participant[i]
            return answer
    
    answer=sorted_participant[len(participant)-1]
    return answer
