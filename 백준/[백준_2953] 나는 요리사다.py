max_score, winner = 0, 0

for candidate in range(5):
    current_score = sum(map(int, input().split()))
    if max_score < current_score:
        max_score = current_score
        winner = candidate+1

print(winner, max_score)
