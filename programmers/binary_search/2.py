# https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    rocks.sort()
    rocks.insert(0, 0)
    rocks.append(distance)    
    distances = [rocks[i] - rocks[i-1] for i in range(1, len(rocks))]
    
    left, right = 1, distance
    mid = (left+right) // 2
    
    while (right-left) > 1:
        current, removed = 0, 0
        for distance in distances:
            current += distance
            if current < mid:
                removed += 1
            else:
                current = 0
        if removed > n:
            right = mid
        else:
            left = mid
        mid = (left+right) // 2

    return mid
