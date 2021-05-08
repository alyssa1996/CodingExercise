def solution(k, room_number):
    answer = []
    checked_in = dict()
    for room in room_number:
        number = room
        visited = [number]
        while number in checked_in:
            number = checked_in[number]
            visited.append(number)
        answer.append(number)
        for room_num in visited:
            checked_in[room_num] = number + 1
    return answer
