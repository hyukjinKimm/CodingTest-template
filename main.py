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
  


INF = 1e9
p =  1000000007


            

  

if __name__ == "__main__": 
  n, m = map(int, input().strip().split())
  if n == m:
     print(0)
     print(1)
     sys.exit()
  dis = [-1] * (100001)
  dis[n] = 0
  q = deque([(n, 0)])
  res = 0
  
  while(q):
     x, d = q.popleft()
     if x == m:
        res += 1
        continue
     for next in [x-1, x+1, 2*x]:
        if 0 <= next <= 100000 and (dis[next] == -1 or dis[next] == d+1):
          q.append((next, d+1))
          dis[next] = d+1 
  print(dis[m])
  print(res)
  
 