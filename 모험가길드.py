import sys

sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
g = 0 
res = 0
for a in arr:
    g += 1
    if g >= a:
        res += 1
        g = 0 
print(res)
