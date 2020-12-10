def fibonacciModified(t1, t2, n):
    temp=list()
    temp.append(t1)
    temp.append(t2)
    for i in range(n):
        last=len(temp)
        temp.append(temp[last-2]+(temp[last-1])**2)
    return temp[n-1]
