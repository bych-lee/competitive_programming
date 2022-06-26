# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    sec = 0
    s = 0
    while q:
        sec += 1
        s -= q.pop(0)
        if truck_weights:
            if s + truck_weights[0] <= weight:
                b = truck_weights.pop(0)
                q.append(b)
                s += b
            else:
                q.append(0)
    return sec
