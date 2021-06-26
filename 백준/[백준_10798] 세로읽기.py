words = []
max_length = 0
for _ in range(5):
    current_line = input()
    words.append(current_line)
    if max_length < len(current_line):
        max_length = len(current_line)

answer = ''
for j in range(max_length):
    for i in range(5):
        if len(words[i]) < j+1:
            continue
        answer += words[i][j]
        
print(answer)
