import sys
import heapq
from collections import deque
from itertools import combinations
import copy
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

L, C  = map(int, input().split())
arr = list(input().split())
arr.sort()
for item in combinations(arr, L):
    v = 0
    c = 0
    for x in item:
        if x in 'aeiou':
            v += 1
        else:
            c += 1
    if v >= 1 and c >= 2:
        print("".join(sorted(item)))
    