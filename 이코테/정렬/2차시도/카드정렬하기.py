import sys
from collections import deque
import heapq
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]





if __name__ == "__main__":
  N = int(input())
  cards = []
  for i in range(N):
    heapq.heappush(cards, int(sys.stdin.readline().strip()))
  res = 0
  for i in range(N-1):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    res += (a+b)
    heapq.heappush(cards, a + b)
  print(res)
    