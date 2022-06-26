# https://atcoder.jp/contests/abc256/tasks/abc256_e

N = int(input())
X = list(map(int, input().split()))
C = list(map(int, input().split()))

is_visited = [False] * N
frustration = 0

for n in range(N):
    graph = []
    while not is_visited[n]:
        is_visited[n] = True
        graph.append(n)
        n = X[n] - 1
    for i in range(len(graph)):
        if graph[i] == n:
            cycle = graph[i:]
            frustration += min([C[x] for x in cycle])
            break

print(frustration)
