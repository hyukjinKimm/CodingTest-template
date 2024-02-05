import sys
from collections import deque
from itertools import combinations_with_replacement
from itertools import combinations
from itertools import permutations
from itertools import product
from bisect import bisect_left, bisect_right
import heapq
import math
import copy


sys.setrecursionlimit(10**7)
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline


            


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]






INF = int(1e9)


  

   
    


if __name__=="__main__":
 s = list(input().strip())
 bomb = input().strip()
 length = len(bomb)

 
 while(1):
   stack = []
   flag = True
   for c in s:
   
     stack.append(c)
     if "".join(stack[-length:]) == bomb:
       flag = False 
       for i in range(length):
         stack.pop()
   
   s = stack[:]
   if len(s) == 0:
     print("FRULA")
     break 
   if flag:
     print("".join(s))
     break 
   

     
       
       
       
     
       
     
     
  