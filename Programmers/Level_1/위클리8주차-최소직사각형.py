def solution(sizes):
    max_w, max_h = 0, 0
    for idx, size in enumerate(sizes):
        current_w, current_h = size[0], size[1]
        if current_w < current_h:
            sizes[idx] = [current_h, current_w]
            current_w, current_h = current_h, current_w
        if max_w < current_w:
            max_w = current_w
        if max_h < current_h:
            max_h = current_h
            
    return max_w*max_h
