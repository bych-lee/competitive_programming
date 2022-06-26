# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

from collections import Counter

def solution(participant, completion):
    for p in participant:
        if p not in completion:
            return p
        else:
            completion.remove(p)
