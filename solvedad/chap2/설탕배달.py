

if __name__ == "__main__":
  n = int(input())
  if n < 5 and n != 3:
    print(-1)
  else:
    for f in range(n//5, -1, -1):
      tmp =  n - 5*f
      if tmp % 3 == 0:
        print(f + tmp//3)
        break 
    else:
      print(-1)

