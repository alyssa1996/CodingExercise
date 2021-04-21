from itertools import combinations
def solution(nums):
    answer = 0
    combi = list(combinations(nums,3))
    
    for value in combi:
        current = sum(value)
        check = True
        for num in range(2,int(current**(1/2))+1):
            if current % num == 0:
                check = False
                break
        if check:
            answer += 1

    return answer
