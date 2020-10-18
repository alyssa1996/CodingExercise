def solution(arr):
    index=1
    answer=[arr[0]]
    while index<len(arr):
        if not arr[index] == arr[index-1]:
            answer.append(arr[index])
        index+=1
    return answer
