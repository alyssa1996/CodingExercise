def can_jump(stones, k, mid):
    jump_count = k
    for stone in stones:
        if stone <= mid:
            jump_count -= 1
            if jump_count == 0:
                return False
        else:
            jump_count = k
    return True

def solution(stones, k):
    answer = 0
    left, right = 0, 1e9
    while left <= right:
        mid = (left+right)//2
        if can_jump(stones, k, mid):
            answer = mid
            left = mid +1
        else:
            right = mid - 1
    
    return answer + 1
