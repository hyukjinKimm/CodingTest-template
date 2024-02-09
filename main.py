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


            


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]





INF = float('inf')

mod = 1000000007

  

  






if __name__=="__main__":
  n = int(input().strip())
  board = []
  sec = 0
  for _ in range(n):
    board.append(list(map(int, input().strip().split())))
  for i in range(n):
    for j in range(n):
      if board[i][j] == 9:
        shark = (i, j)
        break
  size = 2
  acc = 0
  while(1):
    q = deque([(shark[0], shark[1], 0)])
    visited = [[0] * n for _ in range(n)]
    board[shark[0]][shark[1]] = 0
    visited[shark[0]][shark[1]] = 1
    cand = []

    while(q):
      x, y, d = q.popleft()
      for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
          if board[nx][ny] == size or board[nx][ny] == 0:
            visited[nx][ny] = 1
            q.append((nx, ny, d+1))
          elif 0 < board[nx][ny] < size:
            q.append((nx, ny, d+1))
            visited[nx][ny] = 1
            cand.append((nx, ny, board[nx][ny], d+1))
  
    if not cand:
      print(sec)
      break 
    cand.sort(key= lambda x: (x[3], x[0], x[1]))
    tx, ty, ts, td = cand[0]

    board[tx][ty] = 0
    acc += 1

    if acc == size:
      acc = 0
      size += 1
  
    sec += td
    shark = (tx, ty)
    


    








    