# https://atcoder.jp/contests/abc256/tasks/abc256_c

h1, h2, h3, w1, w2, w3 = map(int, input().split())

num = 0
for a11 in range(1, min(h1-1, w1-1)):
  for a12 in range(1, h1-a11):
    for a21 in range(1, w1-a11):
      for a22 in range(1, min(h2-a21, w2-a12)):
        a13 = h1 - (a11 + a12)
        a23 = h2 - (a21 + a22)
        a31 = w1 - (a11 + a21)
        a32 = w2 - (a12 + a22)
        x = h3 - (a31 + a32)
        y = w3 - (a13 + a23)
        if x > 0 and x == y:
          num += 1
          
print(num)
