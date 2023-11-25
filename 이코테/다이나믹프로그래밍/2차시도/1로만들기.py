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
  N =int(input())
  # 1로 가는 최소 계산 횟수들.
  dy = [0] * (N+1)

  for i in range(2, N+1):
    dy[i] = dy[i-1] + 1

    if i % 5 == 0:
      dy[i] = min(dy[i], dy[i//5]+1)
    if i % 3 == 0:
      dy[i] = min(dy[i], dy[i//3]+1)
    if i % 2 == 0:
      dy[i] = min(dy[i], dy[i//2]+1)
  
  print(dy[N])

    

    


    


