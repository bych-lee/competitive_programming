# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    number = [int(x) for x in list(number)]
    flag = True
    for _ in range(k):
        for i in range(1, len(number)):
            if number[i] > number[i-1]:
                del number[i-1]
                flag = False
                break
        if flag == True:
            del number[-1]
    return ''.join([str(x) for x in number])
