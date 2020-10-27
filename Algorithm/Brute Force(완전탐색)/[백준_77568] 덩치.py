people=int(input(""))

info=list()
for i in range(people):
    info.append(input("").split(" "))
    
info_sorted=sorted(info)
result=list()
for i in range(len(info)-1):
    for j in range(i+1,len(info)):
