def get_relationship(family, person):
    parents = [person]
    while person != -1:
        parents.append(family[person])
        person = family[person]
    return parents

import sys
input = sys.stdin.readline
n = int(input())
family = [-1 for _ in range(n+1)]
person1, person2 = map(int, input().split())

m = int(input())
for _ in range(m):
    parent, child = map(int, input().split())
    family[child] = parent

parents_person1 = get_relationship(family, person1)
parents_person2 = get_relationship(family, person2)

count = 0
for idx1, parent1 in enumerate(parents_person1):
    count = idx1
    is_found = False
    for idx2, parent2 in enumerate(parents_person2):
        if parent1 == parent2 == -1:
            print(-1)
        elif parent1 == parent2:
            count += idx2
            print(count)
            is_found = True
            break
    if is_found:
        break
