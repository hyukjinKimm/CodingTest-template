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





dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]





input = sys.stdin.readline

   
if __name__ == "__main__":
  n, m, b = map(int, input().strip().split())
  board = []
  for _ in range(n):
    board.append(list(map(int, input().strip().split())))
  minVal = float('inf')
  maxVal = -1
  for i in range(n):
    for j in range(m):
      minVal = min(minVal, board[i][j])
      maxVal = max(maxVal, board[i][j])

  res = float('inf')
  for g in range(maxVal, minVal-1, -1):
    time = 0
    bb = b
    for x in range(n):
      for y in range(m):
        if board[x][y] > g:
          diff = board[x][y] - g 
          time += diff*2 
          bb += diff
        elif board[x][y] < g:
          bb -= (g-board[x][y])
          time += (g-board[x][y])
        
    if bb >= 0 :
      # 땅고르기가 가능 
      if res > time:
        res = min(res, time)
        indexG = g
  print(res, indexG)


      
          

