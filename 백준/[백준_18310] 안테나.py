import sys
n=int(input())
homes=list(map(int,sys.stdin.readline().split()))
homes.sort()

print(homes[(n-1)//2])

