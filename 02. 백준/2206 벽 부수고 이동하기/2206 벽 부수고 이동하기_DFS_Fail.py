"""
DFS + 백트래킹
"""
import sys


# 좌표 이동량, 우하좌상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def get_min_steps(board, row, col, memo, steps, broken):
    global dx, dy  # 좌표 이동량 전역 변수 선언

    # 현재 위치가 벽인데 이미 벽을 부숴서 부술 수 없다면 그대로 종료
    if board[row][col]:
        if broken:
            return int(1e9)
        broken = True
    # 시간을 더 단축할 수 없는 경우 탐색 종료
    if memo[row][col] <= steps:
        return int(1e9)
    # 목표 도달 시 현재까지 걸어 온 거리 반환
    if row + 1 == len(board) and col + 1 == len(board[0]):
        return steps

    origin_state = board[row][col]
    board[row][col] = 2  # 방문 처리

    for direc in range(4):
        next_r, next_c = row + dx[direc], col + dy[direc]  # 다음 좌표
        # 다음 좌표가 유효하고, 아직 방문하지 않은 곳이라면,
        if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]) \
                and board[next_r][next_c] in [0, 1]:
            memo[row][col] = min(memo[row][col], get_min_steps(board, next_r, next_c, memo, steps + 1, broken))

    board[row][col] = origin_state  # 방문 처리 해제

    return memo[row][col]


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    board = [list(map(int, list(sys_input().rstrip()))) for _ in range(n)]

    memo = [[int(1e9)] * m for _ in range(n)]  # 최소 거리 [행][열]

    answer = get_min_steps(board, 0, 0, memo, 1, False)
    if answer == int(1e9):  # 도달하지 못 한 경우 -1로 변경
        answer = -1
    print(answer)


sys.setrecursionlimit(1000000)
solution()
