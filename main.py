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

import math


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")





dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]









input = sys.stdin.readline


             
   
   
def solution(n, weak, dist):
    w = len(weak)
    for i in range(w):
       weak.append(n+weak[i])
    res = float('inf')
    for i in range(w):
       for friend in permutations(dist, len(dist)):
         cnt = 0
         end = friend[cnt] + weak[i]
         for j in range(i+1, i+w):
            if weak[j] > end:
               cnt += 1
               if cnt >= len(dist):
                  break 
               end = weak[j] + friend[cnt]
            else:
               continue
         else:
            res = min(cnt+1, res)
    if res == float('inf'):
       return -1 
    return res
  

if __name__ == "__main__":
  n = 12
  weak = 	[1, 5, 6, 10]
  dist = [1, 2, 3, 4]
  print(solution(n, weak, dist))