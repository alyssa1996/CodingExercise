def solution(msg):
    answer = []
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
             'S','T','U','V','W','X','Y','Z']
    idx = 0
    while idx < len(msg):
        n_idx = idx+2
        while n_idx <= len(msg):
            if msg[idx:n_idx] not in alphabet:
                break
            else:
                n_idx += 1
        answer.append(alphabet.index(msg[idx:n_idx-1])+1)
        
        if n_idx is not len(msg)-1:
            alphabet.append(msg[idx:n_idx])
        
        idx = n_idx-1
    
    return answer
