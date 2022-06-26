# https://atcoder.jp/contests/abc256/tasks/abc256_b

N = int(input())
A = list(map(int, input().split()))

P = 0
squares = [0] * 4
for a in A:
  squares[0] = 1
  squares = [0] * a + squares
  squares, score = squares[:4], sum(squares[4:])
  P += score
  
print(P)
