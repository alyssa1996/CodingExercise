total=0
for i in range(5):
    time=input("").split(" ")
    s,e=float(time[0]),float(time[1])
    if e-s>1:
        if e-s-1>4:
            total+=4
        else:
            total+=e-s-1

payment=0
if total%1==0:
    payment=total*2*5000
else:
    payment=(total-0.5)*2*5000+5000

if total>=15:
    payment=payment*0.95
if total<=5:
    payment=payment*1.05
    
print("%d"%payment)
