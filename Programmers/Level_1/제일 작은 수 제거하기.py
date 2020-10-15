def solution(arr):
    small=sorted(arr, reverse=True).pop()
    arr.remove(small)
    if len(arr)==0:
        return [-1]
    return arr
