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





dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]












input = sys.stdin.readline
    

        
if __name__ == "__main__":
  n, k = map(int, input().strip().split())
  
  for i in range(1, n+1):
    if n % i == 0:
      k -= 1
      if k == 0:
        print(i)
        break
