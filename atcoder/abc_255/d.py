N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))

S = [A[0]]
for i in range(N-1):
    S.append(S[-1]+A[i+1])

for i in range(Q):
    x = int(input())
    low, high = 0, N # find the upper limit of the interval (a,b] containing x
    while low < high:
        mid = (low+high) // 2
        if x > A[mid]:
            low = mid + 1
        else:
            high = mid

    if high == 0: # low = high
        print(S[-1]-N*x)
    else:
        print((2*high-N)*x + S[N-1] - 2*S[high-1])
