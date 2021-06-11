white = 0
count = 0
for _ in range(8):
    line = input()
    for box in range(white, 8, 2):
        if line[box] == 'F':
            count += 1
    if white :
        white = 0
    else:
        white = 1

print(count)
