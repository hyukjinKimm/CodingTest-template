import sys
from itertools import combinations
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = set()
w = [0] * 11
for a in arr:
  s.add(a)
  w[a] += 1

res = 0
for item in combinations(list(s), 2):
  a = w[item[0]]
  b = w[item[1]]
  res += a*b
print(res)

  
