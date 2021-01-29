'''
사실 다른 사람들의 코드를 보고 이해한 후 작성하기는 했으나 체득하지는 못한 것
같다. 코드만 보면 트리의 레벨(?) 층을 하나씩 늘려나가는 방식으로 진행되는 거고
그 때, 그 전에 있던 노드에 +value와 -value를 하면서 모든 경우의 수를 만들어
나가는 것 같은데, 어떻게 마지막에 tree에서 타겟 넘버의 갯수를 세면 되는지
이해가 되질 않는다. 이 문제는 다시 풀어봐야 할 듯하다.
DFS와 BFS의 개념은 이해하고 있다고 생각했는데,
이건... 이해를 안한 것만 못하지 않을까...?

'''

def solution(numbers, target):
    tree=[0]
    for i in numbers:
        sub=list()
        for j in tree:
            sub.append(j+i)
            sub.append(j-i)
        tree=sub
    return tree.count(target)
