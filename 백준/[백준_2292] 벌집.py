room_number = int(input())
index = 1
candidate = 1
while candidate < room_number:
    candidate += 6*index
    index += 1

print(index)
