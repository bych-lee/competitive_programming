# https://programmers.co.kr/learn/courses/30/lessons/42746

import functools

def comparison(x, y):
    a = x + y
    b = y + x
    return (int(a)-int(b)>0) - (int(b)-int(a)>0)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(comparison), reverse=True)
    answer = str(int(''.join(numbers)))
    return answer
