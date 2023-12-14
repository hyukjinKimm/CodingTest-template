import sys
from collections import deque
import heapq
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]





if __name__ == "__main__":
  N = int(input())
  arr = list(map(int, input().split()))
  lt = 0 
  rt = N-1 
  while(lt<=rt):
    mid = (lt+rt) // 2
    if arr[mid] == mid:
      res = mid 
      break 
    elif arr[mid] > mid:
      rt = mid - 1
    else:
      lt = mid + 1
  print(res)