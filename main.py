import sys
from collections import deque
import heapq
import math
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right

from bisect import bisect_left, bisect_right


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]




    





if __name__ == "__main__":
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  minVal = float('inf')
  for item in combinations(arr, 3):
    if sum(item) <= m:
      if m - sum(item) < minVal:
        minVal = m - sum(item)
        res = sum(item)
  print(res)

