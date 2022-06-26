# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    cursor = 0
    draft = ['A'] * len(name)
    name = [x for x in name]
    
    while draft != name:
        for i in range(len(draft)):
            if draft[cursor + i] != name[cursor + i]:
                cursor = cursor + i
                break
            if draft[cursor - i] != name[cursor - i]:
                cursor = cursor - i
                break
        answer += i
        
        difference = ord(name[cursor]) - ord(draft[cursor])
        answer += min(difference, 26 - difference)
        draft[cursor] = name[cursor]
    return answer
