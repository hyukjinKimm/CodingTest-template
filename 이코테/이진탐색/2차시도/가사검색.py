import sys
from collections import deque
import heapq
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right

from bisect import bisect_left, bisect_right


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def count_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)

    left_index = bisect_left(array, left_value)

    return right_index - left_index


def Count(arr, arr2,q):
 
  n = len(q)

  if q[0] == '?':

    q = q[::-1]
    cnt = q.count('?')
    s = q[:n-cnt]
    sa = s + 'a' * cnt 
    sz = s + 'z' * cnt 
    return count_range(arr2, sa, sz)

  else:
    cnt = q.count('?')
    s = q[:n-cnt]
    sa = s + 'a' * cnt 
    sz = s + 'z' * cnt 
    return count_range(arr, sa, sz)
      





    

def solution(words, queries):
    wordArr = [[] for _ in range(100001)]
    wordArr2 = [[] for _ in range(100001)]
    for w in words:
      wordArr[len(w)].append(w)
      wordArr2[len(w)].append(w[::-1])

    for i in range(100001):
      wordArr2[i].sort()
      wordArr[i].sort()
    
    answer = []

    for q in queries:
      Arr1 = wordArr[len(q)]
      Arr2 = wordArr2[len(q)]
      
      answer.append(Count(Arr1, Arr2, q))
    

    return answer

if __name__ == "__main__":
  words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
  queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
  print(solution(words, queries))


