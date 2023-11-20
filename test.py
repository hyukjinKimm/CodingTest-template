import sys

sys.setrecursionlimit(10**6)
from collections import deque
from  itertools import combinations


board = [list(map(int, input().split())) for _ in range(10)]


paper = [0] * 6
def D(x, y):
  global ans 

  if x == 10:
    ans = min(ans, sum(paper))
    return
  if y == 10:
    D(x+1, 0)
    return

  if board[x][y] == 0:
    D(x, y+1)
    return

  for sz in range(1, 6):
    if is_possible(x, y, sz):
      mark(x, y, sz, 0)
      D(x, y+1)
      mark(x, y, sz, 1)

  
def is_possible(x, y, sz):

  if paper[sz] == 5:
    return False 
  if x + sz > 10 or y + sz > 10:
    return False 
  
  for i in range(sz):
    for j in range(sz):
      if board[x+i][y+j] != 1:
        return False 
  return True
def mark(x, y, sz, v):
  for i in range(sz):
    for j in range(sz):
      board[x+i][y+j] = v
  if v:
    paper[sz] -= 1
  else:
    paper[sz] += 1
  
ans = 25 
D(0, 0)
print(-1 if ans == 25 else ans)