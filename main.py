import sys
from collections import deque
from itertools import combinations_with_replacement
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right
import heapq
import math


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline


            


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


          
       
    


def count_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)

    return right_index - left_index


def solution(words, queries):
  a1 = [[] for _ in range(10001)]
  a2 = [[] for _ in range(10001)]
  
  for w in words:
     a1[len(w)].append(w)
     a2[len(w)].append(w[::-1])
  for i in range(10001):
     a1[i].sort()
     a2[i].sort()
  
  res = []
  for q in queries:
    if q[0] != '?':
       
       start = q.replace('?', 'a')
       end = q.replace('?', 'z')
       res.append(count_range(a1[len(q)], start, end))
    else:
       q = q[::-1]
       start = q.replace('?', 'a')
       end = q.replace('?', 'z')
       res.append(count_range(a2[len(q)], start, end))
  return res

      


   
if __name__=="__main__":
  words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
  queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
  print(solution(words, queries))

