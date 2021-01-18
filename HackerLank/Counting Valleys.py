def countingValleys(steps, path):
    count=0
    current=0
    for i in range(len(path)):
        if path[i]=='U':
            current+=1
        elif path[i]=='D':
            if current==0:
                count+=1
            current-=1
    return count
