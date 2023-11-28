import sys

sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

s = input()
if(len(s) == 1):
    print(1)
    sys.exit()
zero = 0
one = 0 
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            one += 1
        else:
            zero += 1
if zero + one == 0:
    print(0)
else:
    if s[0] == '0':
        zero += 1
    else:
        one += 1
    print(min(zero, one))


