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

import math


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")





dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]





def next_move(x1y1, x2y2, n):
    x1, y1 = x1y1 
    x2, y2 = x2y2
    res = []
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]
        if possible(x1y1, x2y2):
          res.append(((nx1, ny1), (nx2, ny2)))
    
    if x1 == x2:
      if
      for i in [1, -1]:
          res.append(((x1, y1), (x1+i, y1)))
          res.append(((x2, y2), (x2+i, y2)))
    else:
        for i in [1, -1]:
            res.append(((x2, y2), (x2, y2+i)))
            res.append(((x1, y1), (x1, y1+i)))
    return res

def possible(nx1ny1, nx2ny2, n, board):
    x1, y1 = nx1ny1
    x2, y2 = nx2ny2

    if 0 <= x1 < n and 0 <= x2 < n and 0 <= y1 < n and 0 <= y2 < n and board[x1][y1] != 1  and board[x2][y2] != 1:
        return True 
    return False
input = sys.stdin.readline
def solution(board):
    n = len(board)
    visited =[{(0, 0), (0, 1)}]
    q = deque([((0, 0), (0, 1), 0)])

    while(q):
        x1y1, x2y2, d = q.popleft()
        if x1y1 == (n-1, n-1) or x2y2 == (n-1, n-1):
            return d
        # next = [( (x1, y1), (x2, y2) )]
        next = next_move(x1y1, x2y2, n)
        print(next)
        break
        for nx1ny1, nx2ny2 in next:
            if {nx1ny1, nx2ny2} not in visited and possible(nx1ny1, nx2ny2, n, board):
                visited.append({nx1ny1, nx2ny2})
                q.append((nx1ny1, nx2ny2, d+1))
            




if __name__ == "__main__":
 board = [[0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0],
          [0, 1, 0, 1, 1],
          [1, 1, 0, 0, 1],
          [0, 0, 0, 0, 0]]
 print(solution(board))