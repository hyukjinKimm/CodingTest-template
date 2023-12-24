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
from bisect import bisect_left, bisect_right

import math


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")





dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]





input = sys.stdin.readline
   



if __name__ == "__main__":
  for _ in range(int(input().strip())):
    f = input().strip()
    x = int(input().strip())
    if x:
      arr = input().strip()[1:-1].split(',')
    else:
      input()
      arr = []
  
    arr = deque(arr)
    flag = True
    for o in f:
      if o == 'R':
        flag = not flag 
      else:
        if not arr:
          print('error')
          break
        if flag:
          arr.popleft()
        else:
          arr.pop()
    else:
      arr = list(arr)
      if flag:
        print('[' + ",".join(arr)+ "]")
      else:
       print('[' + ",".join(arr[::-1])+ "]")

   
    
    