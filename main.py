import sys
from collections import deque

from itertools import combinations
from itertools import product
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]



def possible(x, y, n, visited):
   x1, y1 = x 
   x2, y2 = y 
   print(x, y)
   
   res = []
   if x1 == x2:
      for i in [-1, 1]:
         if 0 <= x1 + i < n:
           if board[x1+i][y1] == 0 and board[x2+i][y2] == 0 and {(x1+i, y1), (x2+i, y2)} not in visited:
              res.append(((x1+i, y1), (x2+i, y2)))    
   else:
      for i in [-1, 1]:
         if 0 <= y1 + i < n:
           if board[x1][y1+i] == 0 and board[x2][y2+i] == 0 and {(x1, y1+i), (x2, y2+i)} not in visited:
              res.append(((x1, y1+i), (x2, y2+i)))   
 
   return res
      
  
    
def solution(board):
    n = len(board)
   
    visited = []
    visited.append({(0, 0), (0 ,1)})
    q = deque()
    q.append(((0, 0), (0, 1), 0))
    while(q):
       print(q)
       a, b, d = q.popleft()
       
       if (n-1, n-1) == a or (n-1, n-1) == b:
          return d 
       
       pos = possible(a, b, n, visited)
       
       for x, y in pos:
          if (x, y) not in visited:
             visited.append({x, y})
             q.append((x, y, d+1))


if __name__ == "__main__":
  board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]] 
  print(solution(board))