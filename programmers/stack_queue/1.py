# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    count = 0
    while progresses:
        progresses = [min(x + y, 100) for x, y in zip(progresses, speeds)]
        while progresses[0] == 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            if not progresses:
                break
        if count:
            answer.append(count)
            count = 0
    return answer
