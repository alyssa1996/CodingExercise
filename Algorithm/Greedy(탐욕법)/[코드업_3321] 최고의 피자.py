#코드업 https://codeup.kr/problem.php?id=3321
#백준_5545 https://www.acmicpc.net/problem/5545
toppings=int(input(""))
cost_d,cost_t=input("").split(" ")
cost_d,cost_t=int(cost_d),int(cost_t)
d_cal=int(input(""))

best=(d_cal/cost_d)
pizza=[d_cal,cost_d]
t_cal=list()
for i in range(toppings):
    t_cal.append(int(input("")))

t_cal=sorted(t_cal, reverse=True)

for i in t_cal:
    pizza[0]+=i
    pizza[1]+=cost_t
    total=pizza[0]/pizza[1]
    if total<best:
        break
    else:
        best=total

print("%d" %best)
