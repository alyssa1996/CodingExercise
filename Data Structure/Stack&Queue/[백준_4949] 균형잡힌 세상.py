#https://www.acmicpc.net/problem/4949

def check(sen):
    storage=list()
    answer="yes"
    for i in sen:
        if i in ("(","["):
            storage.append(i)
        elif i==")":
            if len(storage)==0:
                answer="no"
                break
            elif storage[-1]=="(":
                storage.pop()
            else:
                answer="no"
                break
        elif i=="]":
            if len(storage)==0:
                answer="no"
                break
            elif storage[-1] =="[":
                storage.pop()
            else:
                answer="no"
                break
    if len(storage)>0:
        answer="no"
    return answer
        

result=list()
while True:
    sentence=input("")
    if sentence==".":
        break
    result.append(check(sentence))

for i in result:
    print(i)
