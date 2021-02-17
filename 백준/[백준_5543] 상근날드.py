burger=[0]*3
drink=[0]*2
for i in range(3):
    burger[i]=int(input())
for i in range(2):
    drink[i]=int(input())
print(min(burger)+min(drink)-50)
