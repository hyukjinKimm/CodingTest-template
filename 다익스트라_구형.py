import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)] #0번은 취급하지 않기위해 n+1길이만큼 생성 -> 노드연결정보

visited = [False]* (n+1) # 방문정보
distance = [INF] * (n+1) # 최단거리테이블

#모든 간성정보를 입력받기
for _ in range(n):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) #a에서부터 b까지 가는 거리가 c다

def get_smallest_node():
    min_value = INF
    index = 0 # 현재 가장 짧은거리를 갖는 노드의 인덱스를 저장
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]: #테이블중에서 방문되기 전 노드중 가장짧은거리를 가지는
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1] #시작노드와 인접한 노드들의 거리 갱신

    for i in range(n-1): #시작노드를 제외한 n-1개의 노드에 대해 반복
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]: #now번째 인덱스 노드와 연결된 노드와 거리 ( 노드, 거리)
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)