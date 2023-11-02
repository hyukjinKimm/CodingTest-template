import sys
import heapq
from collections import deque
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_Parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    n = int(input())
    indegree = [0] * (n + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
    graph = [[] for i in range(n + 1)]
    times = [0] * (n+1)
    for i in range(1, n+1):
        arr = list(map(int, input().split()))
        if len(arr) == 2:
          times[i] = arr[0]
        else:
          times[i] = arr[0]
          for a in arr[1:-1]: # a 는 선수과목 
              graph[a].append(i)  # A -> B 로 이동 가능
              indegree[i] += 1  # 진입 차수 올려주기
    res = [0] * (n+1)

def topology_sort():
    result = []
    q = deque()
    
    # 처음 시작할 때 진입차수가 0인 노드 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            res[i] = times[i]
            
 
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            res[i] = max(res[i], res[now])
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
                res[i] = res[i] + times[i]

    print(res)

topology_sort()
         
