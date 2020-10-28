#https://www.acmicpc.net/problem/2798

import itertools

number,total=input("").split(" ")
number,total=int(number),int(total)
cards=input("").split(" ")
combi=itertools.combinations(cards,3)

maxi=0
for i in combi:
    result=sum(int(j) for j in i)
    diff=total-result
    if diff>=0 and total-maxi>diff:
        maxi=result

print(maxi)
