# V 는 노드 갯수 M 은 find 혹은 union 연산 횟수
def find_parent_non_recursive(parent, x):
  if parent[x] != x:
    return find_parent_non_recursive(parent, parent[x])
  return x

# 두 원소가 속한 집합을 합치기
def union_Parent(parent, a, b): # 시간복잡도: O(V)
  a = find_parent_non_recursive(parent, a)
  b = find_parent_non_recursive(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
 
v, e = map(int, input().split())
parent = [0] * (v + 1)
 
for i in range(1, v + 1):
  parent[i] = i
 
for i in range(e): # 시간복잡도 O(M)
  a, b = map(int, input().split())
  union_Parent(parent, a, b)
 

# 이걸 해줘도 부모 테이블은 변경 안됨. 
print("각 원소가 속한 집합: " , end="")
for i in range(1, v + 1):
  print(find_parent_non_recursive(parent, i), end=" ")
print()
 
print("부모 테이틀: ",end="")
for i in range(1, v + 1):
  print(parent[i], end=" ")