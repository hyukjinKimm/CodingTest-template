import sys
from collections import deque

from itertools import combinations
from itertools import product
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(index, sumVal):
  print(index, sumVal)
  print(cnt)
  global minVal, maxVal
  if index == n:
    minVal = min(minVal, sumVal)
    maxVal = max(maxVal, sumVal)
    return
  for i in range(4):
    if cnt[i] > 0:
      cnt[i] -= 1
      if i == 0:
        sumVal += arr[index]
      elif i == 1:
        sumVal -= arr[index]
      elif i == 2:
        sumVal *= arr[index]
      elif i == 3:
        if sumVal < 0:
          sumVal //= arr[index]
          sumVal *= -1
        else:
          sumVal //= arr[index]

      dfs(index+1, sumVal)
      cnt[i] += 1




if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  cnt = list(map(int, input().split()))
  candidate = ['+', '-', '*', '/']
  minVal = 1000000000
  maxVal = -100000000
  for item in product(candidate, repeat=n-1):

    tmpCnt = [0] * 4
    for c in item:
      if c == '+':
        tmpCnt[0] += 1
      elif c == '-':
        tmpCnt[1] +=1

      elif c == '*':
        tmpCnt[2] +=1

      elif c =='/':
        tmpCnt[3] += 1
    if tmpCnt != cnt:
      continue 

    sumVal = arr[0]
    for i in range(1, n):
      if item[i-1] == '+':
        sumVal += arr[i]
      elif item[i-1] == '-':
        sumVal -= arr[i]
      elif item[i-1] == '*':
        sumVal *= arr[i]
      else:
        if sumVal < 0:
          sumVal *= -1
          sumVal //= arr[i]
          sumVal *= -1
        else:
          sumVal //= arr[i]
    minVal = min(minVal, sumVal)
    maxVal = max(maxVal, sumVal) 
print(maxVal)
print(minVal)



    



