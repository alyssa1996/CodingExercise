number=int(input(""))
cost_a, cost_b=input("").split(" ")
cost_a,cost_b=int(cost_a),int(cost_b)

dough=int(input(""))
topings=list()
for i in range(number):
    topings.append(int(input("")))

topings=sorted(topings)
best=0

total_cost=int(cost_a)+int(cost_b)*number
total_cal=dough+sum(topings)
print("%d"%(total_cal/total_cost))
