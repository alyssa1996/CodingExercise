n, k = map(int, input().split())
numbers = [True]*(n+1)
erased_order = []

for num in range(2, n+1):
    if numbers[num]:
        erased_order.append(num)
        for multiple in range(num*num, n+1, num):
            if numbers[multiple]:
                numbers[multiple] = False
                erased_order.append(multiple)
    if len(erased_order) == k:
        break

print(erased_order[k-1])
