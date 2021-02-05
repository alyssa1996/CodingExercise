def solution(genres, plays):
    answer = []
    playlist=dict()
    for i in range(len(genres)):
        if genres[i] not in playlist.keys():
            playlist[genres[i]]=dict()
            playlist[genres[i]]["sum"]=0
        playlist[genres[i]][i]=plays[i]
        playlist[genres[i]]["sum"]+=plays[i]
        
    while True:
        if len(playlist.values())==0:
            break
        max_genres=0
        for i in playlist.values():
            if i['sum']>max_genres['sum']:
                max_genres=i
        songs=sorted(i.items(),reversed=True,key=lambda item:item[1])
        print(songs)
        del playlist.values()[i]
    return answer
