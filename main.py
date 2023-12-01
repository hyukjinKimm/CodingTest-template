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




# 1 익음 0 익지않음 -1 없음
if __name__ == "__main__":
  n = int(input())
  cand = []
  end = math.sqrt(n)
  # end 는 소수일 수 있다 .
  # 딱 나누어 떨어지면 end + 1까지 가 범위 
  # 소수이면 
  for i in range(1, int(math.sqrt(n))+1):
    cand.append(i**2)

  
  for i in range(1, 4):
    for item in combinations_with_replacement(cand, i):
      if sum(item) == n:
        print(i)
        sys.exit()
  else:
    print(4)