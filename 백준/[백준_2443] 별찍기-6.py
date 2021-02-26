n=int(input())
for i in range(n,0,-1):
    star=2*i-1
    edge=(2*n-1-(2*i-1))//2
    print(' '*edge+'*'*star)
