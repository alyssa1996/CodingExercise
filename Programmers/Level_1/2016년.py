from datetime import date
def solution(a, b):
    week=['MON','TUE','WED','THU','FRI','SAT','SUN']
    
    answer = week[date(2016,a,b).weekday()]
    return answer
