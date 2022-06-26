X, A, D, N = map(int, input().split())

if D == 0:
    num_oper = abs(X-A)
    exit(print(num_oper))
elif D > 0:
    B = A + (N-1)*D
else: # canonicalize since the case when D < 0 is difficult to handle
    B = A
    A = A + (N-1)*D
    D = -D

if X < A:
    num_oper = A - X
elif X > B:
    num_oper = X - B
else:
    offset = (X-A)%D
    num_oper = min(offset, D-offset)

print(num_oper)
