n = int(input())
words = []
for _ in range(n):
    words.append(list(input()))

result = words[0]
for i in range(1, n):
    for j, alpha in enumerate(words[i]):
        if result[j] != alpha:
            result[j] = "?"

print(''.join(result))
