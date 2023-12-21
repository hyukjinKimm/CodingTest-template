import sys
from collections import deque
import heapq
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right

from bisect import bisect_left, bisect_right


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]




if __name__ == "__main__":
  n, m = map(int, input().split())
  e = [[float('inf')] * (n+1) for _ in range(n+1)]
  for i in range(m):
    a, b = map(int, input().split())
    e[a][b] = 1
  for i in range(1, n+1):
    e[i][i] = 0

  for k in range(1, n+1):
    for i in range(1, n+1):
      for j in range(1, n+1):
        e[i][j] = min(e[i][j], e[i][k] + e[k][j])

  # 들어오는 화살표 + 나가는 화살표 = n-1 이면 cnt + =1
  cnt = 0
  res = [0] * (n+1)
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i == j:
        continue
      if e[i][j] != float('inf'):
        res[j] += 1
        res[i] += 1 
  print(res.count(n-1))
