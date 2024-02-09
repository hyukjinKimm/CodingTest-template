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





INF = float('inf')

mod = 1000000007

  

  
      

def dfs(now, acc):
  global res
  if now > 1000000000: return 
  if now == b:
    res = min(res, acc)
    return 
  
  dfs(now*2, acc+1)
  dfs(10*now+1, acc+1)

if __name__=="__main__":
  a, b = map(int, input().strip().split())
  res = INF
  dfs(a, 0)
  if res == INF:
    print(-1)
  else:
    print(res+1)
  


  