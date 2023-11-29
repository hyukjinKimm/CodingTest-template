import sys
from collections import deque
import heapq
import math
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right

from bisect import bisect_left, bisect_right


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x):
  print(x, end = ' ')
  visited1[x] = 1
  for next in graph[x]:
    if visited1[next] == 0:
      dfs(next)
  

def bfs(x):
  visited2[x] = 1
  q = deque([])
  q.append(x)
  while(q):
    now = q.popleft()
    print(now, end = ' ')
    for next in graph[now]:
      if visited2[next] == 0:
        visited2[next] = 1
        q.append(next)

  





if __name__ == "__main__":
  n, m, v = map(int, input().split())
  graph = [[] for _ in range(n+1)]

  for i in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x].append(y)
    graph[y].append(x)
  for i in range(m):
    graph[i].sort()
  
  visited1 = [0] * (n+1)
  visited2 = [0] * (n+1)
 
  dfs(v)
  print()
  bfs(v)
  

  
  
        

      

    


