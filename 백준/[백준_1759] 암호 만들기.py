from itertools import combinations
l, c = map(int, input().split())
alphabets = set(input().split())
vowel = alphabets & {'a', 'e', 'i', 'o', 'u'}
consonant = alphabets - vowel
passwords = []

for v in range(1, len(vowel)+1):
    if l-v < 2:
        break
    current_vowel = list(combinations(vowel, v))
    current_consonant = list(combinations(consonant, l-v))
    for cv in current_vowel:
        for cc in current_consonant:
            passwords.append(''.join(sorted(cv+cc)))

passwords.sort()
for password in passwords:
    print(password)
    
    
