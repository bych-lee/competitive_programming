# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    candidate = []

    for i in range(len(citations)+1):
        if sum([True for x in citations if x >= i]) >= i:
            candidate.append(i)
            
    h_index = max(candidate)
    return h_index
