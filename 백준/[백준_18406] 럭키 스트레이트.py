score=input()
front=sum([int(i) for i in score[:len(score)//2]])
end=sum([int(i) for i in score[len(score)//2:]])
if front==end:
    print("LUCKY")
else:
    print("READY")
