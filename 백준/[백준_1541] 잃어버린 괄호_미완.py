from itertools import permutations
ex = list(input())
list_ex = []
operator_order = []
previous = 0
for idx,value in enumerate(ex):
    if not value.isnumeric():
        list_ex.append(''.join(ex[previous:idx]))
        list_ex.append(ex[idx])
        previous = idx + 1
        operator_order.append(len(list_ex)-1)

list_ex.append(''.join(ex[previous:]))
operator_order = list(permutations(operator_order, len(operator_order)))
print(operator_order)

result = 1e9
for oper_set in operator_order:
    temp_ex = list_ex.copy()
    print()
    for idx in oper_set:
        print("current : ",''.join(temp_ex[idx-1:idx+2]))
        temp_ex[idx-1:idx+2] = str(eval(''.join(temp_ex[idx-1:idx+2])))
        print(temp_ex)

    temp_ex = eval(''.join(temp_ex))
    if temp_ex < result:
        result = temp_ex

print(result)
