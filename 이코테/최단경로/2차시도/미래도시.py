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

if __name__ == "__main__":
  N, M = map(int, input().split())
  graph = [[] for _ in range(N+1)]

  for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
  X, K = map(int, input().split())
  
  start = 1
  distance =[float('inf')] * (N+1)

  res = 0
  dijkstra(start)
  res += distance[K]

  start = K
  distance =[float('inf')] * (N+1)
  dijkstra(start)
  
  res += distance[X]

  if res == float('inf'):
     print(-1)
  else:
     print(res)







    


