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
  n = int(input())
  arr = list(map(int, input().split()))
  arr.sort()
  m = int(input())
  brr = list(map(int, input().split()))
  for b in brr:
    lt = 0 
    rt = n-1
    while(lt<=rt):
      mid = (lt+rt) // 2
      if arr[mid] == b:
        print(1)
        break
      elif arr[mid] > b:
        rt = mid - 1
      else:
        lt = mid + 1
    else:
      print(0)