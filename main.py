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

def solution(s):
    n = len(s)
    answer = n 

    for i in range(1, n//2+1):
        cnt = 1
        word = s[:i]
        compress = ""
        for j in range(i, n, i):
            if s[j:j+i] == word:
                cnt += 1
                continue
            if cnt == 1:
                compress += word 
                word = s[j:j+i]
            else:
                compress = compress + str(cnt) + word
                cnt = 1
                word = s[j:j+i]
        else:
            if cnt == 1:
                compress += word 
            else:
                compress = compress + str(cnt) + word 

            answer = min(answer, len(compress))
            
    
    return answer

if __name__ == "__main__":
 s = "xababcdcdababcdcd"
 print(solution(s))