import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret
  
def check(board, N):
    for i in range(N):
        for j in range(N):
            if board[N+i][N+j] != 1:
                return False 
    else:
        return True
def solution(key, lock):
    M = len(key)
    N = len(lock)
    board = [[0] * (3*N) for _ in range(3*N)]
    for i in range(N):
        for j in range(N):
            board[N+i][N+j] = lock[i][j]

    for k in range(4):
        key = rotate_90(key)
        for i in range(2*N):
            for j in range(2*N):

                for x in range(M):
                    for y in range(M):
                        board[i+x][j+y] += key[x][y]
                else:
                    if check(board, N):
                        
                        return True

                    else:
                        for x in range(M):
                            for y in range(M):
                                board[i+x][j+y] -= key[x][y]
    else:
        return False



if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))