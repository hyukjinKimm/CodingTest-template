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
  T = int(input())
  for t in range(T):
     N, M = map(int, input().split())
     arr = list(map(int, input().split()))
     board = [arr[i * M:(i + 1) * M] for i in range((len(arr) + M - 1) // M )] 
     dy = [[0] * M for _ in range(N)]
     for i in range(N):
        dy[i][0] = board[i][0]
   
     for j in range(1, M): # 세로
        for i in range(N): # 가로 
           cand = []
           for k in [-1, 0, 1]:
              nx = i + k 
              ny = j - 1
              if 0 <= nx < N and 0 <= ny < M:
                 cand.append(dy[nx][ny])
           dy[i][j] = max(cand) + board[i][j]
 
     maxVal = -1
     for i in range(N):
        maxVal = max(maxVal, dy[i][M-1])
     print(maxVal)
        
        
            
              
           


    


