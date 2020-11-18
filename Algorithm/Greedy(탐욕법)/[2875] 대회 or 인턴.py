n,m,k=map(int,input().split())

remain=0
team=n//2
if n%2!=0:
    remain+=1

if m>team:
    remain+=(m-team)
elif m<team:
    remain+=(team-m)*2
    team=m

while remain<k:
    if team==0:
        break
    team-=1
    remain+=3

print(team)
    
