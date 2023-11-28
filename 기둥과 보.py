import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def possible(build, n, k):
   x = len(build)
   
   for i in range(x):
      x, y, a = build[i]
      if a == 0: #기둥
        if y == 0:
           continue
        
        if [x-1, y, 1] in build or [x, y-1, 0] in build or [x, y, 1] in build:
           continue
        return False
        
    
      

      else: # 보 
        if [x, y-1, 0] in build or [x+1, y-1, 0] in build or ([x-1, y, 1] in build and [x+1, y, 1] in build):
           continue
        return False 
   return True
    
           
         


def solution(n, build_frame):
    build = []
    # x y a(0 기둥 1보) b(0삭제 1설치) 
    for i in range(len(build_frame)): # 1000
        x, y, a, b = build_frame[i]
        if b == 0:
            build.remove([x, y, a]) # 1000
            if not possible(build, n, i+1):
              build.append([x, y, a])
        else:
          build.append([x, y, a])
          if not possible(build, n, i+1):
             build.pop()
    build.sort()
    return build

if __name__ == "__main__":
   n = 5
   build_frame = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
   print(solution(n, build_frame))



        