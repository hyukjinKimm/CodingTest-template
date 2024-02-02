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


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline


            


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]





      










    


    


  



        



  




  
def dfs(x, y, c, s):
  global res
  if c == 4:
    res = max(res, s)
    return 
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:

      visited[nx][ny] = 1
      if c == 2:
        dfs(x, y, c+1, s+board[nx][ny])
        
      
      dfs(nx, ny, c+1, s+board[nx][ny])
      visited[nx][ny] = 0
      


  

if __name__=="__main__":
  n, m = map(int, input().strip().split())
  board = []
  for _ in range(n):
    board.append(list(map(int, input().strip().split())))
  visited = [[0] * m for _ in range(n)]
  res = -1
  for i in range(n):
    for j in range(m):
      visited[i][j] = 1
      dfs(i,j,1,board[i][j])
      visited[i][j] = 0
  print(res)