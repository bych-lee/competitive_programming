# https://atcoder.jp/contests/abc256/tasks/abc256_d

N = int(input())
I = [list(map(int, input().split())) for _ in range(N)]
I.sort()

l0, r0 = I[0]
for l1, r1 in I[1:]:
  if r0 < l1:
    print(l0, r0)
    l0, r0 = l1, r1
  else:
    r0 = max(r0, r1)
print(l0, r0)
