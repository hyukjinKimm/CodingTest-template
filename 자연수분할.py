# 경우의 수만 출력
def P(n, k):
  print(n, k)
  if memo[n][k] != -1: return memo[n][k]
  if n == k or k == 1: return 1
  if n < k: return 0 

  memo[n][k] = P(n-1, k-1) + P(n-k, k)
  return memo[n][k]


n = 1
k = 3 

memo = [[-1] * (k+1) for _ in range(n+1)]



# 자연수 n 을 m 개 이하의 자연수 분할로 나누는 모든 경우의 수
for i in range(1, m+1):
  arr = [list(x) for x in H(range(n-1, 0, -1), i) if sum(x) == n]
  print(arr)
print(P(n, k))


#자연수n 을 m 개 이하의 자연수로 분할하는 모든 경우의 수

def P(n, s, index):
  if s == N:
    for r in range(index):
      print(result[r], end = ' ')
    print()
    return 

  if index == K: return
  
  for i in range(n, 0, -1):
    if index == 0 or result[index-1] >= i:
      result[index] = i
      P(n-i, s+i, index+1)

if __name__ == "__main__":
  N, K = 7, 3
  result = [0] * K
  P(N, 0, 0)
