import sys
from collections import deque
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


sys.stdin=open("input.txt", "r")
input = sys.stdin.readline

INF = 1e9



def dfs(now):
 global cnt
 visited[now] = 1
 next = arr[now]
 if visited[next] == 0:
  dfs(next)
 elif fin[next] == 0:
  tmpNode = next 
  while(1):
   cnt += 1
   tmpNode = arr[tmpNode]
   if tmpNode == next:
    break 
 fin[now] = 1





   
 fin[now] = 1
   


 



if __name__=="__main__":
 for _ in range(int(input().strip())):
  cnt = 0
  n = int(input().strip())
  arr = [-1] + list(map(int, input().strip().split()))
  visited = [0] * (n+1)
  fin = [0] * (n+1)
  for i in range(1, n+1):
   if visited[i] == 0:
    dfs(i)
  print(n-cnt)