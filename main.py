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




    

if __name__ == "__main__":
  n, m = map(int, sys.stdin.readline().strip().split())
  board = []
  for _ in range(n):
    board.append(list(map(int,list(sys.stdin.readline().strip()))))

  

  visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
  
  
  visited[0][0][0] = 1


  c = 0 
  q = deque([])
  q.append((0, 0, 1, 0))

  
  while(q):
    x, y, d, c= q.popleft() # c = 1 벽을 뿌수고옴 c = 0 벽을 안뿌수고 옴.

    if x == n-1 and y == m-1:
      print(d)
      break
    for i in range(4):
      nx = x  + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
     
        if board[nx][ny] == 1 and c == 0 and visited[nx][ny][1] == 0:
            visited[nx][ny][1] = 1
            q.append((nx, ny, d+1, 1))
        elif board[nx][ny] == 0 and visited[nx][ny][c] == 0:
     
          visited[nx][ny][c] = 1
          q.append((nx, ny, d+1, c))
          
  else:
    print(-1)
 






      