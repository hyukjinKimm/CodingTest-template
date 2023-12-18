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

   
       
    
       

           



# 리스트를 n 개씩 자르는 함수
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

   
if __name__ == "__main__":
  a = input().strip()
  b = input().strip()
  dy = [[0] * (len(b)+1) for _ in range(len(a)+1)]
  for i in range(len(b)+1):
     dy[0][i] = i 
  for i in range(len(a)+1):
     dy[i][0] = i
  for i in range(1, len(a)+1):
     for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
           # 같은 문자일경우 
           dy[i][j] = dy[i-1][j-1]
        else:
           dy[i][j] = min(dy[i-1][j-1], dy[i-1][j], dy[i][j-1]) + 1
  print(dy[len(a)][len(b)])