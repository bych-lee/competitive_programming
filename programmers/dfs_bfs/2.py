# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(computers, v, visited):
        visited[v] = True
        for i in [x for x, y in enumerate(computers[v]) if y == 1]:
            if not visited[i]:
                visited[i] = True
                dfs(computers, i, visited)
    
    for v in range(n):
        if not visited[v]:
            answer += 1
            dfs(computers, v, visited)
    return answer
