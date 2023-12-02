def rotate_90_degree(arr):
    n = len(arr)
    rotate_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate_arr[j][n - 1 - i] = arr[i][j]
    return rotate_arr

def symmetry(arr):
   n = len(arr)
   m = len(arr[0])
  
   symmetry_arr = [[0] * m for _ in range(n)]
   for i in range(n):
      for j in range(m):
         symmetry_arr[i][m-1-j] = arr[i][j]
         
   return symmetry_arr
