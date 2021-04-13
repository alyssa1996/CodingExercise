def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for x in range(len(arr2[0])):
            current=0
            for j in range(len(arr1[0])):
                current+=(arr2[j][x]*arr1[i][j])
            answer[-1].append(current)
    return answer
