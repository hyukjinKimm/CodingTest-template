

board = [[1, 2, 3],
        [4, 5, 6],
        [7, 8 , 9]]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def turn(x1, y1, x2, y2):
  
  pre = board[x1][y1]
  x, y = x1, y1
  d = 0
  while(d < 4):
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx <= x2 and 0 <= ny <= y2):
      d += 1
      continue
    board[nx][ny], pre = pre, board[nx][ny]
    x, y = nx, ny
turn(0, 0, 2, 2)

for i in range(len(board)):
  print(board[i])






