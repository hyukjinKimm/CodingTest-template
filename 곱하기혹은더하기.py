import sys

sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

s = input()
res = 0
if s.count('0') == len(s):
    print(0)
else:
    res = 1 
    for a in s:
        if a != '0':
            res *= int(a)
    else:
        print(res)

