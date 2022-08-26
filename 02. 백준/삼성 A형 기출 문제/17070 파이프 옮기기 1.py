"""
재귀 함수로 (i, j)에 파이프를 두었을 때 최대 방법의 수 구하기
    1. 직전에 놓은 파이프의 종류에 따라 (i, j)에 각 파이프를 두었을 때 방법의 수를 찾는다.
        1) 직전 == 가로 -> 가로 or 대각
        2) 직전 == 세로 -> 세로 or 대각
        3) 직전 == 대각 -> 가로 or 세로 or 대각
        => 직전 != 가로 -> 세로 or 대각
        => 직전 != 세로 -> 가로 or 대각
        ==> 가로든 세로든 대각은 항상 실행
"""
import sys


def counting(board, r, c, pipe, memo):
    """
    :param board: 각 지점의 상태 (벽 or 빈 칸)
    :param r: 직전에 놓은 파이프의 끝 행
    :param c: 직전에 놓은 파이프의 끝 열
    :param pipe: 파이프의 종류 (가로: 0, 대각: 1, 세로: 2)
    :param memo: 각 지점에서 파이프를 배치했을 때 경우의수를 저장할 2차원 리스트
    :return: 직전 pipe 상태와 현재 위치한 r, c 지점에 따라 다음 파이프를 배치했을 때 경우의수
    """
    if r + 1 == len(board) and c + 1 == len(board):
        return 1
    if memo[pipe][r][c] != -1:  # 해당 지점에서 놓을 경우의수가 0일 수도 있음
        return memo[pipe][r][c]

    memo[pipe][r][c] = 0
    if r + 1 < len(board) and board[r + 1][c] == 0 and pipe != 0:  # != 가로 -> 세로
        memo[pipe][r][c] += counting(board, r + 1, c, 2, memo)
    if c + 1 < len(board) and board[r][c + 1] == 0 and pipe != 2:  # != 세로 -> 가로
        memo[pipe][r][c] += counting(board, r, c + 1, 0, memo)
    if r + 1 < len(board) and c + 1 < len(board) \
            and board[r + 1][c] == board[r][c + 1] == board[r + 1][c + 1] == 0:  # 대각
        memo[pipe][r][c] += counting(board, r + 1, c + 1, 1, memo)

    return memo[pipe][r][c]


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    board = [list(map(int, sys_input().split())) for _ in range(n)]
    memo = [[[-1] * n for _ in range(n)] for _ in range(3)]

    # (1, 1), (1, 2)에 가로 파이프를 놓고 시작
    print(counting(board, 0, 1, 0, memo))


solution()
