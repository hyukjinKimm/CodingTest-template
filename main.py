import sys
from collections import deque
import heapq
import math
from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import combinations_with_replacement
from bisect import bisect_left, bisect_right

from bisect import bisect_left, bisect_right

import math


sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")





dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]




input = sys.stdin.readline

   
       
    
       

           


INF = 1e9
if __name__ == "__main__":

# 처음 모든 수가 소수(True)로 초기화(0, 1 제외) 
    a, n = map(int, input().strip().split())
    array = [True for i in range(n+1)]
    array[1] = False
    # 2부터 n의 제곱근까지 모든 수를 확인
    for i in range(2, int(math.sqrt(n)) + 1):
    # i가 소수인경우(False를 제외하고 남은 수인 경우)
        if array[i] == True:

    # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j = j + 1

    # 모든 소수 출력
    for i in range(a, n+1):
        if array[i]:
            print(i)