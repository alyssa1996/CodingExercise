def sockMerchant(n, ar):
    colors=dict()
    
    for i in ar:
        if i in colors:
            colors[i]+=1
        else:
            colors[i]=1
    
    count=0
    for v in colors.values():
        count+=v//2
    
    return count
