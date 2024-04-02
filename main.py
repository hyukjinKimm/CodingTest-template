import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline 


# 3을 2개로 
2 + 1 
# 결과 출력함수
# 결과 출력함수
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
