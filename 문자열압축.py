import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

   
  

def solution(s):
    n = len(s)
    res = n
    # 
    for i in range(1, len(s)//2+1):
        word = s[:i]
        compress = ''
        cnt = 1
        for j in range(i, n, i):
            if s[j:j+i] == word:
                cnt += 1
            else:
                if cnt == 1:
                    compress += word 
                else:
                    compress = compress + str(cnt) + word 
                word = s[j:j+i]
                cnt = 1
        else:
            if cnt == 1:
                compress += word 
            else:
                compress = compress + str(cnt) + word 
     
        if len(compress) < res:
            res = len(compress)

       
    return res



if __name__ == "__main__":
    s =	"abcabcabcabcdededededede"
    print(solution(s))