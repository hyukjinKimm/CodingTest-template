import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]



if __name__ == "__main__":
  n, _ = map(int, input().split())
  board = []
  for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))
  visited = [[0] * n for _ in range(n)]
  s, target_x, target_y = map(int, input().split())
  q = []
  for i in range(n):
    for j in range(n):
      if board[i][j] != 0:
        visited[i][j] = 1
        q.append((i, j, board[i][j], 0))
  q.sort(key=lambda x:x[2])
  
  q = deque(q)
  while(q):
    x, y, k, now = q.popleft()
    if now == s:

      print(board[target_x-1][target_y-1])
      break

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 0:
        visited[nx][ny] = 1
        board[nx][ny] = k 
        q.append((nx, ny, k, now+1))
  else:
      print(board[target_x-1][target_y-1])
    
        