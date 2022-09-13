"""
BFS 미치겄네
"""
import sys
from collections import deque


def set_min_dist(board, visit, memo, bfs_q, dx, dy, group_num):
    while bfs_q:
        row, col = bfs_q.popleft()
        board[row][col] = group_num

        for direc in range(4):
            next_r, next_c = row + dx[direc], col + dy[direc]
            if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]):
                memo[next_r][next_c] = min(memo[next_r][next_c], memo[row][col] + 1)
                if not visit[next_r][next_c] and board[next_r][next_c] == 0:
                    visit[next_r][next_c] = True
                    bfs_q.append((next_r, next_c))


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    board = [list(map(int, list(sys_input().rstrip()))) for _ in range(n)]

    # 좌표 이동량, 우하좌상
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    visit = [[False] * m for _ in range(n)]
    visit[0][0] = True

    memo = [[int(1e9)] * m for _ in range(n)]  # 최소 거리 [행][열]
    memo[0][0] = 1

    # 시작점에서 각 지점으로의 최단거리 설정
    connected = True  # 시작점의 구역, 끝점의 구역이 연결되어 있는지

    # 시작 구역과 끝 구역을 나눈 이유는, 구역 연결 시 서로 다른 구역을 연결해야 하기 때문
    set_min_dist(board, visit, memo, deque([(0, 0)]), dx, dy, 2)  # 시작 구역 번호: 2

    # 시작점, 끝점이 연결되어 있지 않을 경우 끝점에서도 BFS
    if memo[-1][-1] == int(1e9):
        connected = False
        memo[-1][-1] = 1
        set_min_dist(board, visit, memo, deque([(n - 1, m - 1)]), dx, dy, 3)  # 끝 구역 번호: 3

    answer = int(1e9)
    for r in range(n):
        for c in range(m):
            if board[r][c] != 1:
                continue

            # 벽일 경우 공간을 이어줄 수 있는지 확인하고 최단거리 갱신
            adj_info = []  # 인접 지점의 거리 정보
            for direc in range(4):
                next_r, next_c = r + dx[direc], c + dy[direc]
                if 0 <= next_r < n and 0 <= next_c < m \
                        and board[next_r][next_c] in [2, 3]:
                    adj_info.append((memo[next_r][next_c], board[next_r][next_c]))
            adj_info.sort()

            if not adj_info:
                continue

            if connected:  # 연결되어 있으면 얼마나 단축이 되는지 알아야 하므로 (최대 거리 - 최소 거리)
                diff = adj_info[-1][0] - adj_info[0][0]
                answer = min(answer, memo[-1][-1] - diff + 2)
            else:  # 연결되어 있지 않다면 2, 3번 구역의 최소 거리 두 개를 합쳐야 함
                max_2, max_3 = None, None
                for elem, area in adj_info:
                    if area == 2:
                        if max_2 is None or max_2 > elem:
                            max_2 = elem
                    elif area == 3:
                        if max_3 is None or max_3 > elem:
                            max_3 = elem
                if max_2 and max_3:
                    answer = min(answer, max_2 + max_3 + 1)

    print(answer if answer != int(1e9) else -1)


solution()
