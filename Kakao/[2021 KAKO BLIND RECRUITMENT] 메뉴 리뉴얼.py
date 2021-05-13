from collections import defaultdict
from itertools import combinations
def solution(orders, course):
    menu = {count:defaultdict(int) for count in course}
    answer = []
    for order in orders:
        for key, dic in menu.items():
            if len(order) < key:
                continue
            candidates = list(combinations(order, key))
            for candidate in candidates:
                candidate = ''.join(sorted(list(candidate)))
                dic[candidate] += 1

    for key, dic in menu.items():
        if not dic:
            continue
        max_menu = max(dic.values())
        if max_menu == 1:
            continue
        for name, value in dic.items():
            if value == max_menu:
                answer.append(name)

    return sorted(answer)
