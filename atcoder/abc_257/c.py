N = int(input())
S = list(map(int, input()))
W = list(map(int, input().split()))

SW = sorted(list(zip(S, W)), key=lambda x: x[1])
current = sum(S)
maximum = current

for i in range(N):
    if SW[i][0] == 0:
        current += 1
    else:
        current -= 1

    if i < N-1:
        if SW[i][1] != SW[i+1][1]:
            maximum = max(maximum, current)
    else:
        maximum = max(maximum, current)

print(maximum)
