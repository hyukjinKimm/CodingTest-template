import sys
from collections import deque
from itertools import combinations_with_replacement
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right
import heapq
import math
import copy


sys.setrecursionlimit(10**7)
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline


            


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]





INF = float('inf')

mod = 1000000007

  

  


# left_value <= x <= right_value
def count_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)

    return right_index - left_index



  

if __name__=="__main__":
  s = input().strip()
  n = len(s)
  yn = [[False] * (n) for _ in range(n)]

  for i in range(n):
     yn[i][i] = True 

  for i in range(n-1):
     if s[i] == s[i+1]:
        yn[i][i+1] = True

  for length in range(3, n+1):
    for start in range(0, n-length+1):
       end = start + length - 1 
       if s[start] == s[end] and yn[start+1][end-1]:
          yn[start][end] = True
  
  dy = [float('inf')] * (n+1)
  dy[0] = 0 
  dy[1] = 1
  for end in range(2, n+1):
     for start in range(1, end+1):
        if yn[start-1][end-1]:
           dy[end] = min(dy[end], dy[start-1]+1)
           
  print(dy)
  print(dy[n])

  

 