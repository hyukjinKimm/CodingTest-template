import sys
from collections import deque

from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def count_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

def solution(N, stages):
    stages.sort()
  
    p = [0] * (N+2)
    for i in range(1, N+2):
       p[i] = count_range(stages, i, i)
 
    rest = sum(p)
   
    for i in range(1, N+1):
       # 이미 스테이지에 도달한 플레이어 수
       tmp = p[i]
       if rest > 0:
         p[i] = p[i] / rest
      
       rest -= tmp

    res = [(2, 0)]
    for i in range(1, N+1):
       res.append((p[i], i))
   
    res.sort(key= lambda x: (-x[0], x[1]))
    realres = []
    for i in range(1, N+1):
       realres.append(res[i][1])
   
    return realres



if __name__ == "__main__":
  N = 4
  stages = 	[4,4,4,4,4]
  print(solution(N, stages))
  