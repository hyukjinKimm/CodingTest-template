import sys
from collections import deque
import heapq
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right

from bisect import bisect_left, bisect_right


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]




if __name__ == "__main__":
  N = int(input())
  t = [0]
  p = [0]
  for i in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    t.append(a)
    p.append(b)
  dy = [0] * (N+2)

 
  for i in range(N, 0, -1):
    if t[i] + i <= N+1:
      dy[i] = max(p[i] + dy[t[i]+i], dy[i+1])
    else:
      dy[i] = dy[i+1]
  print(dy[1])


           


    


