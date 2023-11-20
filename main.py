import sys

sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

N, K = map(int, input().split())
res = 0
while(N >= K):
    res += (N-(N//K)*K)
    N -= (N-(N//K)*K)
    N = N // K 
    res += 1
res += (N-1)
print(res)
    