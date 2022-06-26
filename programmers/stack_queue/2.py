# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    queue =  [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        one = queue.pop(0)
        if any([one[1] < another[1] for another in queue]):
            queue.append(one)
        else:
            answer += 1
            if one[0] == location:
                return answer
