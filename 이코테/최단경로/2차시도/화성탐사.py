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



INF = int(1e9)
def dijkstra():
    x = y = 0
    distance[x][y] = graph[x][y]
    q = []
    q.append((distance[x][y], x, y))
  

	# 큐가 빌때까지
    while q:
       
        dist, x, y = heapq.heappop(q) # 거리가 가장 짧은 노드를 큐에서 꺼낸다.
        # 현재 노드가 이미 처리된적 있는 노드라면 무시 -> 방문이 되었는지 확인하는것과 같은원리
        # 현재 꺼낸 그 원소의 거리값(dist)이 테이블에 기록되어있는 값보다 더 크다면 이미 처리된것
        if distance[x][y] < dist:
          continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
              cost = dist + graph[nx][ny]
              if cost < distance[nx][ny]: #현재노드를 거쳐가는것과 기존의 값을 비교
                  distance[nx][ny] = cost
                  heapq.heappush(q, (cost, nx, ny))


if __name__ == "__main__":
 t = int(input())
 for i in range(t):
  n = int(input())
  graph = []
  for i in range(n):
   graph.append(list(map(int, input().split())))
  distance = [[INF] * (n) for _ in range(n)]
  dijkstra()
  print(distance[n-1][n-1])



  


# 다익스트라 알고리즘 - 방문처리여부를 확인 필요X

  