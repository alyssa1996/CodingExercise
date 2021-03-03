def bfs(index,visited,graph):
    if visited[index]:
        return 
    visited[index]=True
    for i in range(len(graph[index])):
        bfs(graph[index][i],visited,graph)

def solution(n, computers):
    answer = 0
    graph=[]
    visited=[False]*n
    
    for i in range(n):
        graph.append([])
        for j in range(n):
            if i==j:
                continue
            if computers[i][j]:
                graph[-1].append(j)

    for i in range(n):
        if len(graph[i])==0:
            answer+=1
            continue
        if visited[i]==False:
            bfs(i,visited,graph)
            answer+=1
        
    return answer
