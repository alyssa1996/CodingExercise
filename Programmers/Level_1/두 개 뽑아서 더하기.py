def solution(numbers):
    answer = []
    numbers=sorted(numbers)
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    answer=sorted(answer)
    return answer
