import sys
from collections import deque
import heapq
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]





def Count(x):
  cnt = 1
  n = len(h)
  last = h[0]
  for i in range(1, len(h)):
    if h[i] - last >= x:
      cnt += 1
      last = h[i]
  return cnt

if __name__ == "__main__":
  N, C = map(int, input().split())
  h = []
  for i in range(N):
    h.append(int(sys.stdin.readline().strip()))
  h.sort()
  lt= 1 
  rt = h[-1] - h[0]
  while(lt<=rt):
    mid = (lt+rt) // 2
    if Count(mid) >= C:
      res = mid 
      lt = mid + 1
    else:
      rt = mid - 1
  print(res)
    



