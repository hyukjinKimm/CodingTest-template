if __name__ == "__main__":
  a, b , v = map(int, input().split())
  if ((v-a) % (a-b) == 0):
    print((v-a)//(a-b) + 1)
  else:
    print(int((v-a)/(a-b)+2))
  

          