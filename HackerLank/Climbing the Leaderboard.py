def searchLank(target,ranking,ranked,start,end):
    if start>=end:
        if target<ranked[start]:
            return ranking[start]+1
        else:
            return ranking[start]
    middle=(start+end)//2
    if target<ranked[middle]:
        return searchLank(target,ranking,ranked,middle+1,end)
    elif target==ranked[middle]:
        return ranking[middle]
    else:
        return searchLank(target,ranking,ranked,start,middle-1)

def climbingLeaderboard(ranked, player):
    ranking=list()
    player_rank=list()
    ranking.append(1)
    
    for i in range(1,len(ranked)):
        if ranked[i-1]>ranked[i]:
            ranking.append(ranking[-1]+1)
        else:
            ranking.append(ranking[-1])
    
    for i in player:
        index=searchLank(i,ranking,ranked,0,len(ranked)-1)
        player_rank.append(index)
    
    return player_rank
