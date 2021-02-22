for i in range(3):
    play=input().split()
    if play.count('0')==0:
        print('E')
    elif play.count('0')==1:
        print('A')
    elif play.count('0')==2:
        print('B')
    elif play.count('0')==3:
        print('C')
    else:
        print('D')
