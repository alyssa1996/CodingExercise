def solution(files):
    file_store = []
    for idx, file in enumerate(files):
        head, number = '', ''
        for char_idx, char in enumerate(file):
            if char.isnumeric():
                while char_idx < len(file) and file[char_idx].isnumeric():
                    number += file[char_idx]
                    char_idx += 1
                break
            else:
                head += char
        file_store.append((head.lower(), int(number), idx))
    
    file_store.sort()
    return [files[idx] for head, number, idx in file_store]
