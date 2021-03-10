from bisect import bisect_left,bisect_right

def count_by_range(a,left,right):
    left_index=bisect_left(a,left)
    right_index=bisect_right(a,right)
    return right_index-left_index

def solution(words, queries):
    answer =  []
    array=[[] for i in range(10001)]
    reversed_array=[[] for i in range(10001)]
    
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    for target in queries:
        if target[0] !='?':
            result=count_by_range(array[len(target)],target.replace('?','a'),target.replace('?','z'))
        else:
            result=count_by_range(reversed_array[len(target)],target[::-1].replace('?','a'),target[::-1].replace('?','z'))
        answer.append(result)
    return answer
