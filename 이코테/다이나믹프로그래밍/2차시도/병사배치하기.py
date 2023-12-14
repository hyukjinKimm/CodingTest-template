import sys
from collections import deque
import heapq
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
  N = int(input())
  arr = list(map(int, input().split()))
 
  dy = [0] * N
  dy[0] = 1
  for i in range(1, N):
    for j in range(i):
      if arr[j] > arr[i]:
        dy[i] = max(dy[j], dy[i])
    dy[i] += 1
  print(dy)
  print(N-max(dy))
 


    


