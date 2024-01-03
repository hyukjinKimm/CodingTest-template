import sys
def rotate_90_degree(arr):
    n = len(arr)
    rotate_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate_arr[j][n - 1 - i] = arr[i][j]
    return rotate_arr


# 2차원 리스트 y 축 대칭 함수
def symmetry(arr):
   n = len(arr)
   m = len(arr[0])
  
   symmetry_arr = [[0] * m for _ in range(n)]
   for i in range(n):
      for j in range(m):
         symmetry_arr[i][m-1-j] = arr[i][j]
         
   return symmetry_arr

test = [[1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 1, 1]]
for i in range(4):
    print(test[i])
print()
new = symmetry(test)
for i in range(4):
    print(new[i])





# 리스트를 n 개씩 자르는 함수
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


# a를 b 번곱한 수를 c 로 나눈 결과 (a**b)%c
a,b,c = map(int,sys.stdin.readline().split())
def multi (a,n):
  if n == 1:
      return a%c
  else:
      tmp = multi(a,n//2)
      if n %2 ==0:
          return (tmp * tmp) % c
      else:
          return (tmp  * tmp *a) %c
multi(a, b)

# 약수 `갯수구하기 시간복잡도  O(N**(1/2))
def getMyDivisor(n):

    res = 0

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            res += 1
            if ( (i**2) != n) : 
                res += 1

    return res

# 이항계수 구하기 
def bino_coef(n, k):
    if k == 0 or n == k:
        return 1
    return bino_coef(n-1, k) + bino_coef(n-1, k-1)
# bino_coef(4, 2)
# 6

# 행렬곱셈
def mul(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)): 
        lists = []
        for j in range(len(arr2[0])): 
            for k in range(len(arr1[0])): 
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer


# 두 선분의 교차 판별  check 함수로 확인.

def ccw(p1, p2, p3):
    temp = (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])
    if temp > 0:
        return 1
    elif temp == 0:
        return 0
    else:
        return -1
    
def check(p1, p2, p3, p4):
    
    is_result = False
    result = 0
    p123 = ccw(p1, p2, p3)
    p124 = ccw(p1, p2, p4)
    p341 = ccw(p3, p4, p1)
    p342 = ccw(p3, p4, p2)

    if p123 * p124 == 0 and p341 * p342 == 0:
        is_result = True
        if min(p1[0], p2[0])<=max(p3[0],p4[0]) and min(p3[0],p4[0])<=max(p1[0],p2[0]) and min(p1[1],p2[1])<=max(p3[1],p4[1]) and min(p3[1],p4[1])<=max(p1[1],p2[1]):
            result = 1

    if p123 * p124 <= 0 and p341 * p342 <= 0:
        if not is_result:
            result = 1
        
    return result   