import sys
from collections import deque
from itertools import combinations_with_replacement
from itertools import combinations
from itertools import permutations
from itertools import product
import heapq
import math


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline


            



      






dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]



    


      
           
def solution(n, weak, dist):
    lw = len(weak)
    res = float('inf')
    for i in range(lw):
       weak.append(weak[i]+n)
    for friends in permutations(dist, len(dist)):
       for start in range(lw):
          now = 0
          until = 0
          for pos in range(start, start+lw):
            if weak[pos] > until:
              now += 1
              if now > len(dist):
                  break
              until = weak[pos] + friends[now-1]
          else:
             res = min(now, res)

          
    if res == float('inf'):
       return -1
    return res
if __name__=="__main__":
  n = 12
  weak = 	[1, 3, 4, 9, 10]
  dist = [3, 5, 7]
  print(solution(n, weak, dist))