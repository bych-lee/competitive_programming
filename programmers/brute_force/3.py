# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):    
    for y in range(1, int((brown+4) / 2)):
        x1 = (brown+4)/2 - y
        x2 = (brown+yellow) / y
        if x1 == x2:
            return [x1, y]
