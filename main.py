import sys
import heapq
from collections import deque
from itertools import combinations
import copy
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")
# V 는 노드 갯수 M 은 find 혹은 union 연산 횟수
# 특정 원소가 속한 집합을 찾기
# V 는 노드 갯수 M 은 find 혹은 union 연산 횟수
def find_parent_non_recursive(parent, x):
  if parent[x] != x:
    return find_parent_non_recursive(parent, parent[x])
  return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent_non_recursive(parent, a)
    b = find_parent_non_recursive(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    A, aParent = find_parent_non_recursive(parent, a)
    B, bParent = find_parent_non_recursive(parent, b)

    if aParent == bParent:
        cycle = True
        
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")