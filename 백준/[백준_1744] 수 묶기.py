def sum_all(numbers, length):
    if length % 2 == 0:
        return get_sum(numbers, length)
    else:
        return get_sum(numbers, length-1) + numbers[-1]
    

def get_sum(numbers, length):
    result = 0
    for idx in range(0, length, 2):
        result += numbers[idx]*numbers[idx+1]
    return result

n = int(input())

positive = []
negative = []
result = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num == 1:
        result += 1
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

result += sum_all(positive, len(positive)) + sum_all(negative, len(negative))
print(result)

        
