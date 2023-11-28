import sys

sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
arr. sort()
now = 0
for i in range(n):
    if arr[i] <= now+1:
        now += arr[i]
    else:
        break 
print(now+1)

