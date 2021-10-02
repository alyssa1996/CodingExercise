number = int(input())
N = 1_000_000_000

table = [[0]*10 for _ in range(number+1)]
table[1] = [1,1,1,1,1,1,1,1,1,1]

if number == 1:
    print(sum(table[1][1:]))
else:
    for i in range(2, number+1):
        for j in range(10):
            if j == 0:
                table[i][j] = table[i-1][j+1]
            elif j == 9:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = table[i-1][j-1]+table[i-1][j+1]
    print(sum(table[number][1:])%N)
                
