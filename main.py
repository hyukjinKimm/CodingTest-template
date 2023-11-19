import sys
import heapq
from collections import deque
from itertools import combinations
import copy
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")




def check(x):
    sumVal = 0
    for a in arr:
        if a <= x:
            sumVal += a 
        else:
            sumVal += x 
    else:
        return sumVal

if __name__ == "__main__":
    n = int(input())
   # dy[길이][끝나는수]
    dy  = [[0] * (n+1) for i in range(10)]

    for i in range(1, 10):
        dy[i][1] = 1
    dy[0][1] = 0

    for j in range(2, n+1):
        for i in range(10):
            if i == 0:
              dy[i][j] = dy[i+1][j-1]
            elif i == 9:
              dy[i][j] = dy[i-1][j-1]
            else:
              dy[i][j] += dy[i+1][j-1]
              dy[i][j] += dy[i-1][j-1]
    res = 0
    for i in range(10):
      res += dy[i][n]
    print(res % 1000000000)

    

        