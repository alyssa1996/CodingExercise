from collections import deque
def solution(enter, leave):
    answer = [0]*(len(enter))
    enter = deque(enter)
    leave = deque(leave)
    room = set()
    while enter and leave:
        while leave and leave[0] in room:
            leaved = leave.popleft()
            room.remove(leaved)
        new = enter.popleft()
        for person in room:
            answer[person-1] += 1
        answer[new-1] = len(room)
        room.add(new)
        
    return answer
