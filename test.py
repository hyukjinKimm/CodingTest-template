import time
import sys
import copy
input = sys.stdin.readline
sys.stdin=open("input.txt", "r")

test = [[1, 2, 3]]
b = copy.copy(test)

test[0] = 14
print(b)