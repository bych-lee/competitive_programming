# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    
    for phone_number in phone_book:
        temp = ''
        for number in phone_number:
            temp += number
            if temp in phone_book and temp != phone_number:
                return False
    return True
