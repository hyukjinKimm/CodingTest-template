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





def topology_sort():
   
    result = []
    q = deque()
    
    # 처음 시작할 때 진입차수가 0인 노드 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    certain = True
    cycle = False

    for i in range(n):

      if len(q) > 1:
       certain = False 
       break 
      
      if len(q) == 0:
       cycle = True 
       break 
      
      now = q.popleft()
      result.append(now)

      for i in range(1, n+1):
         if graph[now][i]:
            indegree[i] -= 1
            if indegree[i] == 0:
               q.append(i)

    if not certain:
       print('?')
    elif cycle:
       print("IMPOSSIBLE")
    else:
       for r in result:
          print(r, end = ' ')
       print()
            
         
    



if __name__ == "__main__":
  # 화살표는 높은 등수에서 낮은 등수로
  tc = int(input())
  for i in range(tc):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    indegree = [0] * (n + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
    graph = [[False] * (n+1) for _ in range(n+1)]
    for i in range(n):
      for j in range(i+1, n):
        graph[arr[i]][arr[j]] = True 
        indegree[arr[j]] += 1
  
    
    x = int(sys.stdin.readline().strip())
    for _ in range(x):
      # a b 의 순위가 바뀜
      a, b = map(int, sys.stdin.readline().strip().split())
      # a 가 b보다 순위가 높으면 
      # indegree 는 들어오는 값 
      # a 와 b 의 순위가 바뀜 .

      if graph[a][b]:
        # b 가 a 보다 순위가 높음 

        graph[a][b] = False 
        graph[b][a] = True 

        indegree[a] += 1
        indegree[b] -= 1
      else:
        graph[a][b] = True 
        graph[b][a] = False 

        indegree[a] -= 1
        indegree[b] += 1
    topology_sort()
      



        




        
