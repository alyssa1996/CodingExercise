#코드업 https://codeup.kr/problem.php?id=4833

stick=list(input(""))

result=0
pop_stick=list()
while len(stick)>0:
    now=stick.pop()
    if now=="(":
        pop_stick.pop()
        result+=1
    elif stick[len(stick)-1] == "(":
        stick.pop()
        result+=len(pop_stick)
    else:
        pop_stick.append(now)

print(result)
        
