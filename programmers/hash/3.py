# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter
from functools import reduce

def solution(clothes):
    a = Counter(x[1] for x in clothes)
    return reduce(lambda y, z: y * z, [x + 1 for x in a.values()]) - 1
