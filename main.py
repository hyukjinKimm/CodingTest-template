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




input = sys.stdin.readline
  


INF = 1e9

            

  



def count():
  res = 0
  for i in range(r):
    for j in range(c):
      if board[i][j] > 0:
        res += board[i][j]
  return res 

def spread():
 
# 확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.
  
  dust = deque([])
  for i in range(r):
    for j in range(c):
      if board[i][j] > 0:
        dust.append((i, j))

  tmpBoard = [[0] * c for _ in range(r)]
  while(dust):
    x, y = dust.popleft()
    cnt = 0
    cand = []
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
        cand.append((nx, ny))
        cnt += 1
    if not cand:
      continue
    Arc = board[x][y]
    bit = int(Arc/5)
    for xx, yy in cand:
      tmpBoard[xx][yy] += bit 
    board[x][y] -= cnt*bit
  for i in range(r):
    for j in range(c):
      board[i][j] += tmpBoard[i][j]
  


# 0, 1 
# -1, 0
# 0, -1
# 1, 0

upx = [0, -1, 0, 1]
upy = [1, 0, -1, 0]

# 0, 1
# 1, 0
# 0, -1
# -1, 0
donwx = [0, 1, 0, -1]
donwy = [1, 0, -1, 0]

def upAir():
  x, y = cleaner[0] 
  dir = 0
  x += upx[dir]
  y += upy[dir]
  previous = 0
 
  while(1):
   
    nx = x + upx[dir]
    ny = y + upy[dir]

    if (x, y) == cleaner[0]:
      break 

    if not (0 <= nx < r and 0 <= ny < c):
      dir += 1
      continue

    board[x][y], previous =  previous, board[x][y]
    x = nx 
    y = ny

    





def donwAir():
  x, y = cleaner[1] 
  dir = 0
  x += donwx[dir]
  y += donwy[dir]
  previous = 0
 
  while(1):
    nx = x + donwx[dir]
    ny = y + donwy[dir]

    if (x, y) == cleaner[1]:
      break 

    if not (0 <= nx < r and 0 <= ny < c):
      dir += 1
      continue

    board[x][y], previous =  previous, board[x][y]
    x = nx 
    y = ny



  
  


r, c, t = map(int, input().strip().split())
board = []
for _ in range(r):
  board.append(list(map(int, input().strip().split())))

cleaner = []
for i in range(r):
  if board[i][0] == -1:
    cleaner.append((i, 0))


if __name__ == "__main__": 
  while(t):
    spread()
    upAir()
    donwAir()
    t -= 1
  print(count())
  
  