n=int(input())
h,m,s=0,0,0
count=0
while True:
    if h==n and m==59 and s==59:
        break
    if s==60:
        m+=1
        s=0
    if m==60:
        h+=1
        m=0
    if '3' in str(h) or '3' in str(m) or '3' in str(s):
        count+=1
    s+=1

#모범답안

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
    
print(count)
