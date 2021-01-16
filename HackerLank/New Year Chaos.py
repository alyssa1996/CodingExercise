def minimumBribes(q):
    for i in range(len(q)):
        if q[i]-(i+1)>2:
            print("Too chaotic")
            return
    
    swapCount=0
    while True:
        isSwaped=False
        for i in range(1,len(q)):
            if q[i]<q[i-1]:
                isSwaped=True
                q[i],q[i-1]=q[i-1],q[i]
                swapCount+=1
        if not isSwaped:
            break
    
    print(swapCount)
