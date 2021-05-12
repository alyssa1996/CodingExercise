from itertools import repeat
import math

def get_played_time(start, end):
    start_hour, start_min = map(int, start.split(":"))
    end_hour, end_min = map(int, end.split(":"))
    return (end_hour - start_hour)*60 + end_min - start_min

def change_code(codes):
    code_change = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for target, changed  in code_change.items():
        if target in codes:
            codes = codes.replace(target, changed)
    return codes

def solution(m, musicinfos):
    m = change_code(m)
    answer_title, answer_time = "(None)", 0
    for musicinfo in musicinfos:
        start, end, title, codes = musicinfo.split(",")
        play_time = get_played_time(start, end)
        codes = change_code(codes)
        played_code = codes[:play_time]
        if len(codes) < play_time:
            played_code = ''.join(list(repeat(played_code, math.ceil(play_time/len(codes)))))
        
        if m in played_code and answer_time < play_time:
            answer_title, answer_time = title, play_time
            
    return answer_title
