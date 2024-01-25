import sys
from collections import deque
from itertools import combinations_with_replacement
from itertools import combinations
from itertools import permutations
from itertools import product
import heapq
import math
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline


            



      









if __name__=="__main__":
  s = input().strip()

  d = dict()
  for c in s:
    if d.get(c):
      d[c] += 1
    else:
      d[c] = 1
  cnt = 0
  hol = ''
  for items in d.items():
    if items[1] % 2 != 0:
      cnt += 1
      hol = items[0]
    if cnt == 2:
      print("I'm Sorry Hansoo")
      sys.exit()
  arry = list(d.items())
  arry.sort()
  res = ''
  for c, v in arry:
    res += c*(v//2)
  print(res + hol + res[::-1])
    
  


