h,m=map(int,input().split())
time=int(input())
h+=time//60
m+=time%60
if m>59:
    m-=60
    h+=1
if h>23:
    h-=24
print(h,m)
