t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    room_number=n//h+1
    floor=n%h
    if floor==0:
        floor=h
        room_number-=1
    if room_number<10:
        room=str(floor)+'0'+str(room_number)
    else:
        room=str(floor)+str(room_number)
    print(int(room))
