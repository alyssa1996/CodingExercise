e,s,m=input().split()
e,s,m=int(e),int(s),int(m)

count=1
compare=[1,1,1]
while True:
    if compare[0]==e and compare[1]==s and compare[2]==m:
        break
    if compare[0]==15:
        compare[0]=1
    else:
        compare[0]+=1
    if compare[1]==28:
        compare[1]=1
    else:
        compare[1]+=1
    if compare[2]==19:
        compare[2]=1
    else:compare[2]+=1
    count+=1
print(count)
