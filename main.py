import sys
from collections import deque
import heapq
import math
from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement
from bisect import bisect_left, bisect_right
import re


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")




    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]




input = sys.stdin.readline
  


INF = 1e9

p = 1000000000


def ccw(p1, p2, p3):
    temp = (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])
    if temp > 0:
        return 1
    elif temp == 0:
        return 0
    else:
        return -1
    
def check(p1, p2, p3, p4):
    
    is_result = False
    result = 0
    p123 = ccw(p1, p2, p3)
    p124 = ccw(p1, p2, p4)
    p341 = ccw(p3, p4, p1)
    p342 = ccw(p3, p4, p2)

    if p123 * p124 == 0 and p341 * p342 == 0:
        is_result = True
        if min(p1[0], p2[0])<=max(p3[0],p4[0]) and min(p3[0],p4[0])<=max(p1[0],p2[0]) and min(p1[1],p2[1])<=max(p3[1],p4[1]) and min(p3[1],p4[1])<=max(p1[1],p2[1]):
            result = 1

    if p123 * p124 <= 0 and p341 * p342 <= 0:
        if not is_result:
            result = 1
        
    return result   

     
      


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


if __name__ == "__main__": 
  n = int(input().strip())
  pos = []
  for _ in range(n):
    pos.append(list(map(int, input().strip().split())))
  parent = [0] * (n+1)
  for i in range(1, n+1):
     parent[i] = i 
  for i in range(1, n+1):
     for j in range(i+1, n+1):
        if check(i-1, j-1):
          union_Parent(parent, i, j)
  for i in range(1, n + 1):
    find_parent(parent, i)
  
  res = [0] * (n+1)
  for i in range(1, n+1):
     res[parent[i]] += 1
  print(len(set(parent[1:])))
  print(max(res))
    
    

 
