import sys
from collections import deque
import heapq
import math
from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement
from bisect import bisect_left, bisect_right
import re


import math


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")




    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]




input = sys.stdin.readline
  


INF = 1e9

p = 1000000000


      
    


# left_value <= x <= right_value
def count_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)

    return right_index - left_index


if __name__ == "__main__": 
  T = int(input().strip())
  A = int(input().strip())
  # 접두사 합(Prefix Sum) 배열 계산
  sum_value = 0
  arr = [0]
  for i in list(map(int, input().strip().split())):
      sum_value += i
      arr.append(sum_value)

  B = int(input().strip())
  sum_value = 0
  brr = [0]
  for i in list(map(int, input().strip().split())):
      sum_value += i
      brr.append(sum_value)
  allArr = []
  for left in range(1, A+1): # 첫번째 부터 A 번째 까지 
     for right in range(left, A+1): # left 번째부터 A 번째 까지 
       allArr.append(arr[right] - arr[left-1])
        

  allBrr = []
  for left in range(1, B+1): # 첫번째 부터 A 번째 까지 
     for right in range(left, B+1): # left 번째부터 A 번째 까지 
       allBrr.append(brr[right] - brr[left-1])
  allBrr.sort()

  res = 0
  for x in allArr:
     find = T-x 

     res += count_range(allBrr, find, find)
  print(res)



  
  
  
        
        
  
