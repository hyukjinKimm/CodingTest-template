import heapq
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")
def solution(food_times, k):
    if sum(food_times) <= k: # 전체 음식을 먹는 시간보다 k가 크거나 같으면 -1
        return -1
    
    q = [] 
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) # (음식시간, 음식번호)를 우선순위 큐에 삽입
        
    sum_value = 0 #  먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    # "먹기 위해 사용한 시간 + (현재 음식 시간 - 이전 음식 시간) * 현재 남은 음식 개수" 와 "k" 비교
    while sum_value + ((q[0][0] - previous) * length) <= k: 
        now = heapq.heappop(q)[0] # 현재 음식 시간
        sum_value += (now - previous) * length 
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식을 현재 음식으로
        
    result = sorted(q, key = lambda x: x[1]) # 음식 번호 기준으로 정렬하여 저장
    
    return result[(k - sum_value) % length][1] # 반복문을 돌지는 않지만,

if __name__ == "__main__":
    food_array = [2, 6, 5, 1, 2]
    k = 10
    print(solution(food_array, k))
