n, k = map(int, input().split())
items = [(0,0)]
backpacks = [[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
    weight, value = map(int, input().split())
    items.append((weight, value))

for i in range(1, n+1):
    for j in range(1, k+1):
        weight, value = items[i][0], items[i][1]
        if j < weight:
            backpacks[i][j] = backpacks[i-1][j]
        else:
            backpacks[i][j] = max(value+backpacks[i-1][j-weight], backpacks[i-1][j])

print(backpacks[n][k])
