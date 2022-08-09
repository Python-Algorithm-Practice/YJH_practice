"""

"""
import sys


sys_input = sys.stdin.readline  # 빠른 입력

n = int(sys_input())
orders = sys_input().split()

move = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}  # 방향에 따른 이동거리

r, c = 0, 0  # 시작 위치
for order in orders:
    # 다음 위치를 계산하고 유효 좌표 판별
    next_r = r + move[order][0]
    next_c = c + move[order][1]

    # 유효 좌표라면 해당 좌표로 이동
    if 0 <= next_r < n and 0 <= next_c < n:
        r = next_r
        c = next_c

print(r + 1, c + 1)
