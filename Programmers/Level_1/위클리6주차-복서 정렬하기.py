def solution(weights, head2head):
    answer = []
    for idx, weight in enumerate(weights):
        total_play, win_count, winning_heavier = 0 , 0, 0
        for player, result in enumerate(head2head[idx]):
            if not result == 'N':
                total_play += 1           
            if result == 'W':
                win_count += 1
                if weights[player] > weight:
                    winning_heavier += 1       
        if total_play:
            win = win_count/total_play
        else:
            win = 0
        answer.append((-win, -winning_heavier, -weight, idx+1))
    
    answer.sort()
    return [player for _, _, _, player in answer]
