import sys
from collections import deque
import heapq
import math
from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement
from bisect import bisect_left, bisect_right

from bisect import bisect_left, bisect_right


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]



if __name__ == "__main__":
  n = int(input())
  h = []
  for i in range(n):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    h.append((('R', a), ('G', b), ('B', c)))
  
  res = float('inf')
  for i in range(3):
    color, tmp = h[0][i]
    print(color, tmp)
    for j in range(1, n):
      arr = list(h[j])
      arr.sort(key = lambda x: x[1])
      q = deque(list(arr))
      while(q):
        c, cost = q.popleft()
        if c == color:
          continue
        color = c 
        tmp += cost 
        break
    print(tmp)
      
    res = min(tmp, res)
  print(res)






    



  
