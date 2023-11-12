# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블에서 부모노드를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
        cost, a, b = edge
        #사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
                union_parent(parent, a, b) # 1. 여기서는 parent 테이블이 루트 노드를 가리키지 않을 수도있다.
                                           # 2. 하지만 if 조건절에서 find_parent 를 실행함으로서 업데이트 된 parent 끼리 비교가 가능함.
                result += cost

print(result)