expression = input().split('-')
answer = sum(map(int,expression[0].split('+')))
for i in expression[1:]:
    answer -= sum(map(int,i.split('+')))
print(answer)
