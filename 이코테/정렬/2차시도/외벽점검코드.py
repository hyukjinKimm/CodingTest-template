import sys
from collections import deque

from itertools import combinations
from itertools import permutations
from itertools import product
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]




def solution(n, weak, dist):
    d = len(dist)
    w = len(weak)
    for i in range(w):
       weak.append(n+weak[i])
    res = float('inf')
    
    for friends in permutations(dist, d):
       for start in range(w):
         cnt = 0
         sumVal = weak[start] + friends[cnt]

         for now in range(start+1, start+w):
     
            if weak[now] > sumVal:
               cnt += 1
               if cnt == d:
                  break 
               sumVal = friends[cnt] + weak[now]
            else:
               continue
         else:
            res = min(res, cnt+1)

    if res == float('inf'):
       return - 1
    
    return res
    


if __name__ == "__main__":
  n = 12
  weak =	[1, 3, 4, 9, 10]
  dist = [3, 5, 7]
  print(solution(n, weak, dist))