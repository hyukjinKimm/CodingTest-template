import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기 
n, m = map(int, input().split())
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for _ in range(n+1)] #0번은 취급하지 않기위해 n+1길이만큼 생성 -> 노드연결정보

# 최단거리테이블을 모두 무한으로 초기화
distance = [INF] * (n+1) # 최단거리테이블

#모든 간성정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) #a에서부터 b까지 가는 거리가 c다

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

dijkstra(start)