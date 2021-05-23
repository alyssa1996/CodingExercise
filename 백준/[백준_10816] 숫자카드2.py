N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

cards.sort()
def count_card(target, count, start, end):
    if end <= start:
        return count
    middle = (start+end)//2
    if cards[middle] == target:
        count += 1
        count_card(target, count, start, middle-1)
        count_card(target, count, middle+1, end)
    elif cards[middle] < target:
        count_card(target, count, middle+1, end)
    else:
        count_card(target, count, start, middle-1)

count = []
for target in targets:
    count.append(count_card(target, 0, 0, len(cards)))

print(count)
print(' '.join(count))
