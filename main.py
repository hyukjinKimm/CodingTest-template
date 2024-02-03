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






INF = int(1e9)


def ans(row, col):
  if dy[row][col] != -1: return dy[row][col]
  if row == 0: return board[row][col]
  for i in [-1, 0, 1]:
    nr = row - 1
    nc = col + i 
    if 0 <= nc < 3:
      dy[row][col] = max(dy[row][col], ans(nr, nc) + board[row][col])
  return dy[row][col]

if __name__=="__main__":
  n = int(input().strip())
  board =[]
  for _ in range(n):
    board.append(list(map(int, input().strip().split())))
  dy = [[-1] * 3 for _ in range(n)]
  for i in range(3):
    ans(n-1, i)
  print(dy[n-1])

