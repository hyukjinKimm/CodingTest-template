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





      










    
# 다익스트라 알고리즘 - 방문처리여부를 확인 필요X
def dijkstra(start):
    q = []
    
	#시작 노드로 가기위한 최단경로는 0으로 설정하고 (우선순위)큐에 삽입
    heapq.heappush(q,(0, start)) 
    distance[start] = 0

	# 큐가 빌때까지
    while q:
        dist, now = heapq.heappop(q) # 거리가 가장 짧은 노드를 큐에서 꺼낸다.
        # 현재 노드가 이미 처리된적 있는 노드라면 무시 -> 방문이 되었는지 확인하는것과 같은원리
        # 현재 꺼낸 그 원소의 거리값(dist)이 테이블에 기록되어있는 값보다 더 크다면 이미 처리된것
        if distance[now] < dist:
          continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]: #현재노드를 거쳐가는것과 기존의 값을 비교
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = float('inf')
if __name__=="__main__":
  n, m = map(int, input().strip().split())
  start = int(input().strip())
  graph = [[] for _ in range(n+1)]
  for _ in range(m):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))
  distance = [INF] * (n+1)
  dijkstra(start)
  for x in distance[1:]:
     if x == INF:
        print(-1)
     else:
        print(x)







  
    