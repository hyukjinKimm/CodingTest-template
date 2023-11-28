import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn(nd):
    global d
    if nd == 'L':
      d -= 1
      if d == -1:
          d = 3 
    else:
        d += 1
        if d == 4:
            d = 0 
if __name__ == "__main__":
    n = int(input())
    board =[[0] * n for _ in range(n)]
    for _ in range(int(input())):
        x, y = map(int, sys.stdin.readline().strip().split())
        board[x-1][y-1] = 1
    info = deque([])
    for _ in range(int(input())):
        s, d = sys.stdin.readline().strip().split()
        info.append((int(s), d))
    d = 1
   
    snake = deque([])
    snake.append((0, 0))
   
    
    s = 0
    while(1):

        x, y = snake[-1]
        if info and s == info[0][0]:
            _, nd = info.popleft()
            turn(nd)
      
        
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in snake:
            snake.append((nx, ny))
            if board[nx][ny] == 0:
              snake.popleft()
            else:
                board[nx][ny] = 0
            s += 1

            
        else:
            print(s+1)
            break



        