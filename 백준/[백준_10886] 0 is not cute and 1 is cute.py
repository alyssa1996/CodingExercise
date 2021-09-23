n = int(input())
votes = [int(input()) for _ in range(n)]

if votes.count(0) > votes.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
