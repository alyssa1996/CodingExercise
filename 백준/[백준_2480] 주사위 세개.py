numbers = sorted(list(map(int, input().split())))

if numbers[0] == numbers[2]:
    print(10000+numbers[0]*1000)
elif numbers[0] == numbers[1] or numbers[1] == numbers[2]:
    print(1000+numbers[1]*100)
else:
    print(numbers[2]*100)
