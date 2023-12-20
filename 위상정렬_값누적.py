import sys
import heapq
from collections import deque
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정


def topology_sort():
  
    q = deque()
    
    # 처음 시작할 때 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
      
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(time[i]+result[now], result[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

 

if __name__ == "__main__":
  v = int(input().strip())
  indegree = [0] * (v + 1)
  # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
  graph = [[] for i in range(v + 1)]
  time = [-1]
  result = [-1]
  for b in range(1, v+1):
    arr = list(map(int, input().strip().split()))
    time.append(arr[0])
    result.append(arr[0])
    for a in arr[1:-1]:
      graph[a].append(b)  # A -> B 로 이동 가능
      indegree[b] += 1  # 진입 차수 올려주기
  topology_sort()
  print(result)
  
 