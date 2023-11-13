import math
# 2부터 n까지 모든 수에 대한 소수 판별
n = 1000

# 처음 모든 수가 소수(True)로 초기화(0, 1 제외) 
array = [True for i in range(n+1)]

# 2부터 n의 제곱근까지 모든 수를 확인
for i in range(2, int(math.sqrt(n)) + 1):

# i가 소수인경우(False를 제외하고 남은 수인 경우)
    if array[i] == True:

# i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j = j + 1

# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end= ' ')