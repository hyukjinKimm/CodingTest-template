import sys
from collections import deque
import heapq
import math
from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement
from bisect import bisect_left, bisect_right

from bisect import bisect_left, bisect_right

import math


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")





dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]












input = sys.stdin.readline
    

        
def dfs(x, s, t):
  global res
  if t > k:
    return
  if x == n:
    res = max(res, s)
    return

  dfs(x+1, s+st[x][0], t+st[x][1])
  dfs(x+1, s, t)
if __name__ == "__main__":
  n, k = map(int, input().strip().split())
  st = []
  for i in range(n):
    st.append(list(map(int, input().strip().split())))
  res = -1
  dfs(0,0,0)
  print(res)