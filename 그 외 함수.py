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
