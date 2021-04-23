import re
def solution(new_id):
    new_id = re.sub("\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\=|\+|\[|\{|\]|\}|\:|\?|\,|\<|\>|\/",
                    "",new_id.lower())
    
    changed_id = [new_id[0]]
    for idx in range(1,len(new_id)):
        if new_id[idx] == changed_id[-1] == '.':
            continue
        changed_id.append(new_id[idx])
    
    if changed_id and changed_id[0] == '.':
        changed_id.pop(0)
    if changed_id and changed_id[-1] == '.':
        changed_id.pop()
    if not changed_id:
        changed_id.append('a')
    
    if len(changed_id) >= 16:
        changed_id = changed_id[:15]
    if changed_id[-1] == '.':
        changed_id.pop()
    
    if len(changed_id) <= 2:
        while len(changed_id) < 3:
            changed_id.append(changed_id[-1])
    
    return ''.join(changed_id)
