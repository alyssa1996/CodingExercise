#https://codeup.kr/problem.php?id=3301

money=int(input(""))
change=[50000,10000,5000,1000,500,100,50,10]
result=0
for i in change:
    if money//i>0:
        result+=money//i
        money=money%i

print(result)
