# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    winner = []
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    extended_patterns = list(map(lambda x: x * (len(answers) // len(x)) + x[: len(answers)%len(x)], patterns))
    scores = list(map(lambda x: sum([True if y[0] == y[1] else False for y in zip(answers, x)]), extended_patterns))
    
    max_score = max(scores)
    for index, score in enumerate(scores):
        if score == max_score:
            winner.append(index + 1)
    winner.sort()
    return winner
