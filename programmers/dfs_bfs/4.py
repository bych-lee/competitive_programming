# https://programmers.co.kr/learn/courses/30/lessons/43164

def dfs(tickets, path):
    if not tickets:
        return path
    for y in [y for x, y in tickets if x == path[-1]]:
        tickets2 = tickets[:]
        path2 = path[:]
        
        tickets2.remove([path[-1], y])
        path2.append(y)
        
        answer = dfs(tickets2, path2)
        if answer:
            return answer
        
def solution(tickets):
    tickets.sort()
    return dfs(tickets, ['ICN'])
