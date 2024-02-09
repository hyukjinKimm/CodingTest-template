import sys
from collections import deque
from itertools import combinations_with_replacement
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right
import heapq
import math
import copy


sys.setrecursionlimit(10**7)
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline


            


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]





INF = float('inf')

mod = 1000000007

  

  
def ans(x, y, d):
  
  if dy[x][y][d] != -1: return dy[x][y][d]

  dy[x][y][d] = 0

  if board[x][y] == 1: return 0
  if d == 0:
    dy[x][y][d] += ans(x, y-1, 0)
    dy[x][y][d] += ans(x, y-1, 1)
  elif d == 1:
    if board[x-1][y] == 1 or board[x][y-1] == 1:
      dy[x][y][d] = 0
    else:
      dy[x][y][d] += ans(x-1, y-1, 0)
      dy[x][y][d] += ans(x-1, y-1, 1)
      dy[x][y][d] += ans(x-1, y-1, 2)
  else:
    dy[x][y][d] += ans(x-1, y, 1)
    dy[x][y][d] += ans(x-1, y, 2)
  return dy[x][y][d]



      




if __name__=="__main__":
  n = int(input().strip())
  board = []
  for _ in range(n):
    board.append(list(map(int, input().strip().split())))
  dy = [[[-1, -1, -1] for _ in range(n)] for _ in range(n)]
  
  dy[0][0] = [0, 0, 0]
  dy[0][1] = [1, 0, 0]
 
  for i in range(2, n):
    if board[0][i] == 0:
      dy[0][i] = dy[0][i-1][:]
    else:
      dy[0][i] = [0, 0, 0]
  for i in range(n):
    dy[i][0] = [0, 0, 0]

  for k in range(3):
    ans(n-1, n-1, k)
    
   

  print(sum(dy[n-1][n-1]))
