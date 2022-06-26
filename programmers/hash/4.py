# https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3

def solution(genres, plays):
    answer = []
    dictionary = {g: [] for g in set(genres)}
    
    for item in zip(genres, range(len(plays)), plays):
        dictionary[item[0]].append((item[1], item[2]))
    reference = sorted(dictionary.keys(), key=lambda x: sum([y[1] for y in dictionary[x]]), reverse=True)
    
    for genre in reference:
        temp = [x[0] for x in sorted(dictionary[genre], key=lambda x: (-x[1], x[0]))]
        answer += temp[:min(len(temp), 2)]
    return answer
