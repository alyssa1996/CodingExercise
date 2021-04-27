m = int(input())
n = int(input())

dec_num = []
for cnum in range(m,n+1):
    if cnum == 1:
        continue
    check = True
    for number in range(2,int(cnum**(1/2))+1):
        if not cnum % number:
            check = False
            break
    if check:
        dec_num.append(cnum)

if dec_num:
    print(sum(dec_num))
    print(sorted(dec_num)[0])
else:
    print(-1)
