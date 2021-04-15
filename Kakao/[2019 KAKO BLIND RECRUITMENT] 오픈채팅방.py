user={}
answer=[]

def message(operation,uid):
    current_user=user[uid]
    if operation=='Enter':
        return current_user+'님이 들어왔습니다.'
    if operation=='Leave':
        return current_user+'님이 나갔습니다.'

def solution(record):
    for i in range(len(record)):
        user_info=record[i].split()
        if user_info[0]=='Leave':
            continue
        uid=user_info[1]
        name=user_info[2]
        user[uid]=name
    
    for i in range(len(record)):
        user_info=record[i].split()
        if user_info[0]=='Change':
            continue
        answer.append(message(user_info[0], user_info[1]))
    return answer
