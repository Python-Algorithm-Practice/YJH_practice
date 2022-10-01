"""
2차원 누적합 사용, O(N^2)

왜?
    1. N (1 ~ 1024), M (1 ~ 100000) 이므로,
        명령으로 1 1 1024 1024가 M번 입력되면 연산횟수는 1024 * 1024 * 100000으로 난리가 난다.
    2. 값의 변경이 없으므로 각 구역의 합을 미리 구해놓고 활용할 수 있다.

어떻게?
    1. 행에 대해서 누적합 계산 -> 각 행을 1차원 누적합 배열
    2. 열에 대해서 누적합 계산 -> 2차원 누적합 배열 (arr[i][j] : (1, 1) ~ (i, j) 구역의 값을 모두 더한 값)
    3. x1, y1, x2, y2 계산
        arr[x2][y2] - arr[x1][y2] - arr[x2][y1] + arr[x1][y2]
"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())

    # 입력 (누적합 변환 및 편하게 사용하기 위해 사이즈를 1씩 증가시켜 선언)
    board = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        board[i][1:] = map(int, sys_input().split())

    # 각 행에 대해 누적합 계산
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            board[i][j] += board[i][j - 1]
    # 각 열에 대해 누적합 계산
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            board[i][j] += board[i - 1][j]

    for _ in range(m):
        x1, y1, x2, y2 = map(int, sys_input().split())
        print(board[x2][y2] - board[x1 - 1][y2] - board[x2][y1 - 1] + board[x1 - 1][y1 - 1])


solution()