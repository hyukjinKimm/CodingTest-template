import sys
from collections import deque
from itertools import combinations_with_replacement
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right
import heapq
import math
import copy


sys.setrecursionlimit(10**7)
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline


            


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]





INF = float('inf')

mod = 1000000007

  

  





if __name__=="__main__":
  n, k = map(int, input().strip().split())
  mv = []
  for _ in range(n):
    mv.append(list(map(int, input().strip().split())))
  mv.sort()
  
  bags = []
  for _ in range(k):
    bags.append(int(input().strip()))
  bags.sort()
  bags = deque(bags)
  
  q = []
  res = 0
  print(mv, bags)
  for i in range(n):
    m, v = mv[i]  #현재 보는 보석의 무게와 가치 
    if m <= bags[0]:
      heapq.heappush(q, -v)
    else: # 보는 보석이 제일 작은 가방 보다 큼..
      # q 에 보석이 있을때 
      # q 에 보석이 없을때 
      bags.popleft()
      if q:
        res += -heapq.heappop(q)

      if not bags:break 
  else:
    print('hi', q, bags)

    if bags:
      while(q):
        res += -heapq.heappop(q)
  print(res)




    
      



