# https://programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while people:
        weight = 0
        weight += people.pop()
        
        if people and weight + people[0] <= limit:
            weight += people.popleft()
            
        answer += 1
    return answer

# you can also do as follows without using pop

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
