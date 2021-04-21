def solution(nums):
    goal = len(nums) // 2
    nums = set(nums)
    if goal <= len(nums):
        return goal
    else:
        return len(nums)
