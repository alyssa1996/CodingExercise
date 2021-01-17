def jumpingOnClouds(c):
    count=0
    i=1
    while i<len(c):
        if i+1==len(c):
            count+=1
            break
        if c[i+1]==0:
            count+=1
            i+=2
        elif c[i]==0:
            count+=1
            i+=1
        else:
            i+=1
    
    return count
