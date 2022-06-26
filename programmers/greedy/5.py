# https://programmers.co.kr/learn/courses/30/lessons/42861

def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    edges = []
    parent = [0] * n
    
    for i in range(len(parent)):
        parent[i] = i
        
    for a, b, cost in costs:
        edges.append([cost, a, b])
    edges.sort()
    
    for cost, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
    return answer
