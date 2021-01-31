price=int(input())
change=1000-price
count=0
changes=[500,100,50,10,5,1]

for i in changes:
    if change//i>0:
        count+=(change//i)
        change=(change%i)
    if change==0:
        break

print(count)
