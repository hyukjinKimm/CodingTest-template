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


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")





dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, dist):
  global res
  res = max(dist, res)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and history[ord(board[nx][ny])-65] == 0:
      history[ord(board[nx][ny])-65] =1
      visited[nx][ny] = 1
      dfs(nx, ny, dist+1)
      visited[nx][ny] = 0 
      history[ord(board[nx][ny])-65] = 0


if __name__ == "__main__":
  n, m = map(int, sys.stdin.readline().strip().split())
  board = []
  for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))
  visited = [[0] * m for _ in range(n)]
  visited[0][0] = 1
  history = [0] * (26)
  history[ord(board[0][0])-65] = 1
  res = -1
  dfs(0, 0, 1)
  print(res)
  
  









      



    
