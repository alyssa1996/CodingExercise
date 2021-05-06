from itertools import permutations

def is_match(uid_set, bid_set):
    for idx, uid in enumerate(uid_set):
        bid = bid_set[idx]
        if len(uid) != len(bid):
            return False
        for alpha in range(len(uid)):
            if not (uid[alpha] == bid[alpha] or bid[alpha] == '*'):
                return False
    return True

def solution(user_id, banned_id):
    answer = []
    for candidate in permutations(user_id, len(banned_id)):
        if is_match(candidate, banned_id):
            candidate = set(candidate)
            if candidate not in answer:
                answer.append(candidate)
    
    return len(answer)
