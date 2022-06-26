# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**(1/2)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    candidate = set()
    
    for length in range(1, len(numbers) + 1):
        candidate = candidate | set(map(lambda x: int(''.join(x)), permutations(numbers, length)))
        
    for x in candidate:
        if is_prime(x):
            answer += 1
    return answer
