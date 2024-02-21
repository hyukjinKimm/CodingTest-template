from collections import deque
import copy



def left(board):
  newBoard = [[0] * n for _ in range(n)]
  for i in range(n):
    cursor = 0
    for j in range(n):
      if board[i][j] != 0:
        if newBoard[i][cursor] == 0:
          newBoard[i][cursor] = board[i][j]
        elif newBoard[i][cursor] == board[i][j]:
          newBoard[i][cursor] *= 2
          cursor += 1
        else:
          cursor += 1
          newBoard[i][cursor] = board[i][j]
          
  return newBoard
def right(board):
  newBoard = [[0] * n for _ in range(n)]
  for i in range(n):
    cursor = n-1
    for j in range(n-1, -1, -1):
      if board[i][j] != 0:
        if newBoard[i][cursor] == 0:
          newBoard[i][cursor] = board[i][j]
        elif newBoard[i][cursor] == board[i][j]:
          newBoard[i][cursor] *= 2
          cursor -= 1
        else:
          cursor -= 1
          newBoard[i][cursor] = board[i][j]
          
  return newBoard

def down(board):
  newBoard = [[0] * n for _ in range(n)]
  for j in range(n):
    cursor = n-1
    for i in range(n-1, -1, -1):
      if board[i][j] != 0:
        if newBoard[cursor][j] == 0:
          newBoard[cursor][j] = board[i][j]
        elif newBoard[cursor][j] == board[i][j]:
          newBoard[cursor][j] *= 2
          cursor -= 1
        else:
          cursor -= 1
          newBoard[cursor][j] = board[i][j]
          
  return newBoard

def up(board):
  newBoard = [[0] * n for _ in range(n)]
  for j in range(n):
    cursor = 0
    for i in range(n):
      if board[i][j] != 0:
        if newBoard[cursor][j] == 0:
          newBoard[cursor][j] = board[i][j]
        elif newBoard[cursor][j] == board[i][j]:
          newBoard[cursor][j] *= 2
          cursor += 1
        else:
          cursor += 1
          newBoard[cursor][j] = board[i][j]
  return newBoard



board = [[4, 2, 2], 
         [8, 2, 4], 
         [8, 8, 16]]
n = 3
new = down(board)
for j in range(n):
  print(new[j])

new = up(board)
print()
for j in range(n):
  print(new[j])

new = left(board)
print()
for j in range(n):
  print(new[j])
new = left(new)
print()
for j in range(n):
  print(new[j])
