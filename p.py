a = [[1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]]

def turn(arr):
  new = [[0] * len(arr) for _ in range(len(arr))]
  n = len(arr)
  for i in range(n):
    for j in range(n):
      new[j][n-1-i] =  a[i][j]
  return new 

ans = turn(a)
for i in range(len(ans)):
  print(ans[i])