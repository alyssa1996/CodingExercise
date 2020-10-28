#백준 https://www.acmicpc.net/problem/2231
number=int(input(""))
result=1
while result<number:
    total=result+sum(int(i) for i in list(str(result)))
    if total==number:
        break
    else:
        result+=1

if result>=number:
    print(0)
else:
    print(result)
