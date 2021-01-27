def migratoryBirds(arr):
    birds=dict()
    for i in arr:
        if i in birds.keys():
            birds[i]+=1
        else:
            birds[i]=1

    max_bird=1
    for i,v in birds.items():
        if birds[max_bird]<v:
            max_bird=i
        elif birds[max_bird]==v and max_bird>i:
            max_bird=i
    
    return max_bird
