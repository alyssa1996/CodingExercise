def solution(arr):
    next_number=max(arr)+1
    while True:
        check=True
        for i in range(len(arr)):
            if next_number%arr[i]:
                check=False
                break
        if check:
            break
        next_number+=1
    return next_number
