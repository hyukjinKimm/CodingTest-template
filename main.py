import sys
from collections import deque
import heapq
import math
from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement
from bisect import bisect_left, bisect_right
import re


import math


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")





dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ddx = [-1, 0, 1]
ddy = [-1, 0, 1]

input = sys.stdin.readline
  




  
if __name__ == "__main__":
  n, m = map(int, input().strip().split())

  l = [0] * (101)
  s = [0] * (101)
  for _ in range(n):
    a, b = map(int, input().strip().split())
    l[a] = b
  for _ in range(m):
    a, b = map(int, input().strip().split())
    s[a] = b
  
  # q -> (현재위치, 주사위 던진 회수)
  q = deque([(1, 0)])
  visited = []
  while(q):
    
    x, d = q.popleft()
    if x >= 100:
      print(d)
      break
    if l[x] != 0:
      x = l[x]
    elif s[x] != 0:
      x = s[x]
    for i in range(1, 7):
      if (x, i) not in visited:
        visited.append((x, i))
        q.append((x+i, d+1))


  