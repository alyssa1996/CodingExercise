def isEmpty(q):
    if len(q)==0:
        print(-1)
        return True
    return False

orders=int(input(""))

queue=list()
for i in range(orders):
    message=input("")
    if 'push' in message:
        queue.append(int(message[5]))
    if message=='pop':
        if not isEmpty(queue):
            print(queue[0])
            del queue[0]
    if message=="size":
        print(len(queue))
    if message=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    if message=="front":
        if not isEmpty(queue):
            print(queue[0])
    if message=="back":
        if not isEmpty(queue):
            print(queue[-1])
