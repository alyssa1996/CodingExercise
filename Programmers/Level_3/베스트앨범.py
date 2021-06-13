from collections import defaultdict
def get_sum(playlist):
    return -sum([plays for plays, idx in playlist])

def solution(genres, plays):
    answer = []
    genre_music = defaultdict(list)
    for idx, genre in enumerate(genres):
        genre_music[genre].append((plays[idx], idx))
    
    for genre, playlist in genre_music.items():
        playlist.sort(key=lambda x : (-x[0], x[1]))
        genre_music[genre] = playlist
        
    musics = list(genre_music.values())
    musics.sort(key= lambda x : get_sum(x))
    
    for playlist in musics:
        answer.append(playlist[0][1])
        if len(playlist) >= 2:
            answer.append(playlist[1][1])
    return answer
