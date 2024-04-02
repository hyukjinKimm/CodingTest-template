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


# LCS (가장 긴 부분 수열 )

a = input().strip()
b = input().strip()
 
w = len(a)
h = len(b)
 
graph = [[0] * (w + 1) for _ in range(h + 1)]
 
for i in range(1, h+1):
    for j in range(1, w+1):
        if b[i-1] == a[j-1]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = max(graph[i][j-1], graph[i-1][j])
  res = ""
  i = len(b)
  j = len(a)
  maxVal = graph[-1][-1]
  while(1):
      if i == 0 or j == 0: break 
      if graph[i][j] == graph[i][j-1]:
          j -= 1
      elif graph[i][j] == graph[i-1][j]:
          i -= 1
      else:
        
          res += b[i-1]
          maxVal -= 1
          i -= 1
          j -= 1
  print(len(res))
  print(res[::-1])

# LCS (가장 긴 SUBSTRING )

for i in range(1, h+1):
    for j in range(1, w+1):
        if b[i-1] == a[j-1]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = 0


# 최소 편집 거리(Edit Distance) 계산을 위한 다이나믹 프로그래밍
def edit_dist(str1, str2) :
  n = len(str1)
  m = len(str2)

  # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
  dp = [[0] * (m + 1) for _ in range(n + 1)]

  # DP 테이블 초기 설정
  for i in range(1, n + 1) :
    dp[i][0] = i
  for j in range(1, m + 1) :
    dp[0][j] = j

  # 최소 편집 거리 계산
  for i in range(1, n + 1) :
    for j in range(1, m + 1) :
      # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 삽입
      if str1[i-1] == str2[j-1] :
        dp[i][j] = dp[i-1][j-1]
      # 문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
      else : # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
        dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
  
  return dp[n][m]


# 두 문자열을 입력받기
str1 = input()
str2 = input()



import math

# n개 중 r개를 뽑아서 정렬하는 순열의 개수 출력
a = math.perm(n, r)
print(a)

# n개 중 r개를 뽑는 조합의 개수 출력
b = math.comb(n, r)
print(b)

# n개 중 r개를 중복을 허용하여 뽑는 중복 조합의 개수 출력
c = math.comb(n + r - 1, r)
print(c)


# 진수
# base 진법의 string 을 10 진수로 나타냄
int(string, base)

print(int('111',2))
print(int('222',3))
print(int('333',4))
print(int('444',5))
print(int('555',6))
print(int('FFF',16))

# 10진수를 2, 8, 16 진수로 
print(bin(10))
print(oct(10))
print(hex(10))


# 10진수를 n 진수로
import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]