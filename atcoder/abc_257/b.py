N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for l in L:
    if l == K:
        if A[l-1] == N:
            continue
    else:
        if A[l] == A[l-1] + 1:
            continue
    A[l-1] += 1

print(" ".join(map(str, A)))
