def solution(scores):
    answer = ''
    scores = list(map(list, zip(*scores)))
    
    students = []
    for i in range(len(scores)):
        self_eval = scores[i][i]
        students_eval = scores[i][:i]+scores[i][i+1:]
        average = 0
        if self_eval in (max(scores[i]), min(scores[i])) and self_eval not in set(students_eval):
            average = sum(students_eval)/(len(scores)-1)
        else:
            average = sum(scores[i])/len(scores)
        students.append(average)
    
    for score in students:
        if score >= 90:
            answer += 'A'
        elif score >=80:
            answer += 'B'
        elif score >= 70:
            answer += 'C'
        elif score >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer
