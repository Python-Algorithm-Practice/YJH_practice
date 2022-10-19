"""

"""
import sys


def get_total(board, x1, y1, x2, y2):
    if x2 >= len(board) or y2 >= len(board[0]):
        return 0
    return board[x2][y2] - board[x2][y1 - 1] - board[x1 - 1][y2] + board[x1 - 1][y1 - 1]


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    board = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        board[i + 1][1:] = map(int, list(sys_input().rstrip()))

    # 2차원 누적합 구하기
    for i in range(n + 1):
        for j in range(1, m + 1):
            board[i][j] += board[i][j - 1]
    for j in range(m + 1):
        for i in range(1, n + 1):
            board[i][j] += board[i - 1][j]

    max_size = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            total = get_total(board, i, j, i + max_size, j + max_size)
            while total == (max_size + 1) ** 2:
                max_size += 1
                total = get_total(board, i, j, i + max_size, j + max_size)
            if j + max_size > m:
                break
        if i + max_size > n:
            break
    print(max_size ** 2)


solution()
