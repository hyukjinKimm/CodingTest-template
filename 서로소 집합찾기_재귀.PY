def find_parent(parent, x):
  # 루트 노드가 아니면, 루트 노드를 찾을때까지 재귀적으로 찾기
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
 
v, e = map(int, input().split())
parent = [0] * (v + 1)
 
for i in range(1, v + 1):
  parent[i] = i
 
for i in range(e):
  a, b = map(int, input().split())
  union_Parent(parent, a, b)
 
#이걸 해줘야 부모 테이블이 루트 노드로 전부 업데이트 된다.
print("각 원소가 속한 집합: " , end="")
for i in range(1, v + 1):
  print(find_parent(parent, i), end=" ")
print()
 
print("부모 테이틀: ",end="")
for i in range(1, v + 1):
  print(parent[i], end=" ")