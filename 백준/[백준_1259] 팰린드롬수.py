while True:
    target = input()
    if int(target) == 0:
        break
    reversed_target = target[::-1]
    if int(target) == int(reversed_target):
        print('yes')
    else:
        print('no')
