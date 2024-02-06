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


            


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]






INF = int(1e9)

mod = 1000000007

  

    

if __name__=="__main__":
  n, m = map(int, input().strip().split())
  arr = []
  for _ in range(n):
    arr.append(list(map(int, input().strip().split())))
  dy = [[0] * (n+1) for _ in range(n+1)]
  for i in range(1, n+1):
    dy[1][i] = dy[1][i-1] + arr[0][i-1]
    dy[i][1] = dy[i-1][1] + arr[i-1][0]
  for i in range(1, n+1):
    for j in range(1, n+1):
      dy[i][j] = dy[i-1][j] + dy[i][j-1] - dy[i-1][j-1] + arr[i-1][j-1]
  for _ in range(m):
    x1, y1, x2, y2 = map(int, input().strip().split())
    print(dy[x2][y2] + dy[x1-1][y1-1] - dy[x1-1][y2] - dy[x2][y1-1])
  