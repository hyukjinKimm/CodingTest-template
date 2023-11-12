data = [[0] * 8 for _ in range(8)]
from collections import deque
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        result += 1
        return
      
    # 빈 공간에 울타리 설치
    for i in range(8):
        for j in range(8):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
a=  [[1, 2], [3, 2], [1, 1]]
a.sort(key= lambda x: (x[0], x[1]))
print(a)

print('aa' > 'nn')