# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque, defaultdict

def comparison(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    queue = deque([begin])
    distance = defaultdict(int)
    distance[begin] = 0
    
    while queue:
        v = queue.popleft()
        for w in words:
            if distance[w] == 0 and comparison(v, w):
                queue.append(w)
                distance[w] = distance[v] + 1
    return distance[target]
