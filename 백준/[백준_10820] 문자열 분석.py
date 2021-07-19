while True:
    try:
        sentence = input()
        if sentence == '':
            break
        lower, upper, number, blank = (0, 0, 0, 0) #순서대로 소문자 대문자 숫자 공백
        for string in sentence:
            if string.islower():
                lower += 1
            elif string.isupper():
                upper += 1
            elif string.isdigit():
                number += 1
            elif string == ' ':
                blank += 1
        print(lower, upper, number, blank)
    except EOFError:
        break
