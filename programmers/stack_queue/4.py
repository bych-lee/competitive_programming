# https://programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque
def solution(prices):
    
    answer = []
    for i in range(len(prices)):
        count = 0
        for p in prices[i+1:]:
            if prices[i] > p:
                count += 1
                break
            else:
                count += 1
        answer.append(count)
    return answer
