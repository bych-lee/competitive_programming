# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    low, high = 1, max(times)*n
    
    while low != high:
        mid = (low+high) // 2
        if sum([mid // time for time in times]) >= n:
            high = mid
        else:
            low = mid + 1
    return low
