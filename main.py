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


            


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]






INF = float('inf')


def recur(row, col, first_col):

    if row == n:
        return 0

    if dp[row][col] != INF:
        return dp[row][col]
  
    for j in range(3):
        if j == col:
            continue
        elif row == n - 2 and j == first_col:
            continue
        dp[row][col]= min(dp[row][col], recur(row + 1, j, first_col) + rgb[row][col])

    return dp[row][col]

if __name__=="__main__":
    n = int(input().strip())
    rgb = []
    for _ in range(n):
        rgb.append(list(map(int, input().strip().split())))
    ans = float('inf')
  

    for i in range(3):
        dp = [[INF] * 3 for _ in range(n)]
        recur(0, i, i)
        ans = min(ans, dp[0][i])

    print(ans)
    