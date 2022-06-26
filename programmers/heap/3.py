# https://programmers.co.kr/learn/courses/30/lessons/42628

from heapq import heapify, heappop, heappush

def solution(operations):
    heap = []
    for operation in operations:
        action, argument = operation.split()
        if action == 'I':
            heappush(heap, int(argument))
        else:
            if heap:
                if argument == '-1':
                    heappop(heap)
                else:
                    heap = [-x for x in list(heap)]
                    heapify(heap)
                    heappop(heap)
                    heap = [-x for x in list(heap)]
                    heapify(heap)
    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]
