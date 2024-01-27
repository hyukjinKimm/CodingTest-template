import time
import sys
input = sys.stdin.readline
sys.stdin=open("input.txt", "r")

a = '123'
b = a.replace('3', 'a')
print(b, a)