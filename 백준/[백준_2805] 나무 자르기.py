import sys
sys.setrecursionlimit(1000000000)
n, m = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()

def binary_search(start, end, target):
    if end < start:
        return (start+end)//2
    middle = (start+end)//2
    cutted = 0
    for idx in range(len(trees)):
        if middle < trees[idx]:
            cutted += trees[idx] - middle
    if cutted == target:
        return middle
    elif cutted < target:
        return binary_search(start, middle-1, target)
    else:
        return binary_search(middle+1, end, target)

print(binary_search(0, trees[-1], m))
