# https://programmers.co.kr/learn/courses/30/lessons/42627

from heapq import heappush, heappop
from collections import deque

def solution(jobs):
    answer = []
    current = 0
    
    jobs = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    candidate = []
    heappush(candidate, jobs.popleft())
    
    while len(candidate) > 0:
        duration, arrival = heappop(candidate)
        current = max(current + duration, arrival + duration)
        answer.append(current - arrival)
        while len(jobs) > 0 and jobs[0][1] <= current:
            heappush(candidate, jobs.popleft())
        if len(jobs) > 0 and len(candidate) == 0:
            heappush(candidate, jobs.popleft())
    return sum(answer) // len(answer)
