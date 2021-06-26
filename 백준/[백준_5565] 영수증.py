total = int(input())
book_cost = []
for _ in range(9):
    book_cost.append(int(input()))

print(total-sum(book_cost))
