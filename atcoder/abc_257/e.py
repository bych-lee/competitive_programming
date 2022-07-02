N = int(input())
C = list(map(int, input().split(" ")))

min_ = min(C)
maxargmin = max([i for (i, v) in enumerate(C) if v == min_])

q, r = divmod(N, min_)

ans = ""
for i in range(8, maxargmin, -1):
    p, r = divmod(r, C[i] - min_)
    ans += p * str(i+1)
ans += (q-len(ans)) * str(maxargmin+1)

print(ans)
