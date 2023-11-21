import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    length = len(food_times)
    foodAndIndex = []
    for i in range(length):
        foodAndIndex.append((food_times[i], i))
    foodAndIndex.sort()
    q = deque(foodAndIndex)
    previous = 0
    while((q[0][0] - previous) * (length) <= k):
        time, index = q.popleft()
        k -= (time-previous) * (length)
        length -= 1
        previous = time 
  
    tmp = sorted(q, key=lambda x:x[1])
    
    return tmp[k % length][1] + 1
   
  


if __name__ == "__main__":
    food_array = 			[2, 6, 5, 1, 2]
    k = 10
    print(solution(food_array, k))
