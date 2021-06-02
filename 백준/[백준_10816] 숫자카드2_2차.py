import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
number_card = list(map(int, input().split()))
m = int(input())
target_numbers = list(map(int, input().split()))

count_cards = defaultdict(int)
for card in number_card:
    count_cards[card] += 1

result = []
for target in target_numbers:
    result.append(count_cards[target])

print(' '.join(map(str, result)))
