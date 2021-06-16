def solution(lottos, win_nums):
    win_nums = set(win_nums)
    unknown_num = lottos.count(0)
    lotto_num = len(win_nums & set(lottos))
    rank = [6, 6, 5, 4, 3, 2, 1]
    return [rank[lotto_num+unknown_num], rank[lotto_num]]
