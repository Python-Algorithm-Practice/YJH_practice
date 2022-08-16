"""

"""
import sys
from collections import deque
from time import time


def bfs(tray, r, c):
    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]

    bfs_q = deque([[r, c]])
    tray[r][c] = '1'

    while bfs_q:
        cur_r, cur_c = bfs_q.popleft()

        for direction in range(4):
            next_r, next_c = cur_r + nx[direction], cur_c + ny[direction]

            if 0 <= next_r < len(tray) and 0 <= next_c < len(tray[0]) \
                    and tray[next_r][next_c] == '0':
                bfs_q.append([next_r, next_c])
                tray[next_r][next_c] = '1'


def dfs(tray, r, c):
    tray[r][c] = '1'

    if 0 < r and tray[r - 1][c] == '0':
        dfs(tray, r - 1, c)
    if 0 < c and tray[r][c - 1] == '0':
        dfs(tray, r, c - 1)
    if r + 1 < len(tray) and tray[r + 1][c] == '0':
        dfs(tray, r + 1, c)
    if c + 1 < len(tray[0]) and tray[r][c + 1] == '0':
        dfs(tray, r, c + 1)


def solution():
    sys.stdin = open('testcase/testcase.txt')
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    tray = [list(sys_input().rstrip()) for _ in range(n)]

    begin = time()

    answer = 0
    for i in range(n):
        for j in range(m):
            if tray[i][j] == '0':
                # bfs(tray, i, j)
                dfs(tray, i, j)
                answer += 1

    print(answer)

    print(f'실행시간 : {time() - begin} seconds')


solution()
