train = 0
max_people = 0
for _ in range(4):
    off, on = map(int, input().split())
    train = train - off + on
    if max_people < train:
        max_people = train
print(max_people)
