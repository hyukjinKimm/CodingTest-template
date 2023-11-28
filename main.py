import sys
from collections import deque
import heapq
import math
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
  n = int(input())
  info = []
  for i in range(n):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    info.append((i, tmp[0], tmp[1]))
  # 몸무게 역순으로 정렬한다.
  info.sort(reverse=True, key=lambda x:x[1])
  res =[0] * (n)
  cnt = 1
  for i in range(n):
    xi, xw, xh = info[i]
    if res[xi] == 0:
      tmp = 1
      res[xi] = cnt
      for j in range(i+1, n):
        yi, yw, yh = info[j]
        if xw == yw or xh <= yh:
          res[yi] = cnt
          tmp += 1
      cnt += tmp
    
        
    
  for r in res:
    print(r, end = ' ')