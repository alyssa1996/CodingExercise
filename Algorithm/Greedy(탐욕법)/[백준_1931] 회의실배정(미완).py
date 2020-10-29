def check(start, times):
    current=[times[start]]
    now=start+1
    maxi=0
    while True:
        print(current,": ", end=' ')
        if now==len(times):
            if len(current)>maxi:
                maxi=len(current)
            current.pop()
            if len(current)==0 or current[-1]==times[start]:
                break
            else:
                now=times.index(current.pop())+1
                current.append(times[now])
        if current[-1][1]<=times[now][0]:
            current.append(times[now])
            now+=1
        else:
            now+=1
    return maxi

meetings=int(input(""))

times=list()
for i in range(meetings):
    a,b=input("").split(" ")
    times.append([int(a),int(b)])

times=sorted(times)

maxi=0
for i in range(meetings//2):
    result=check(i,times)
    if result>maxi:
        maxi=result

print(maxi)

