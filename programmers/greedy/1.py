# https://programmers.co.kr/learn/courses/30/lessons/42862

from collections import Counter

def solution(n, lost, reserve):
    answer = 0
    
    count = Counter([x for x in range(1, n+1)] + reserve) - Counter(lost)
    for i in lost:
        if i in count:
            count[i] = 1
            continue
        if count[i-1] == 2:
            count[i-1] = 1
            count[i] = 1
            continue
        if count[i+1] == 2:
            count[i+1] = 1
            count[i] = 1
    
    return len(count)
