numbers=int(input(""))

count=0
for i in range(numbers):
    word=input("")
    alphabet=list()
    check=True
    for j in range(len(word)):
        if word[j] in alphabet:
            if word[j-1]==word[j]:
                continue
            else:
                check=False
                break
        else:
            alphabet.append(word[j])

    if check:
        count+=1

print(count)
