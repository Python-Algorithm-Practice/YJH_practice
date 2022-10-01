"""
BOJ 15686 https://www.acmicpc.net/problem/15686
itertools.combinations 사용
"""
import sys
from itertools import combinations


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    houses = []
    stores = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                houses.append((r, c))
            elif board[r][c] == 2:
                stores.append((r, c))

    # 치킨집을 살릴 수 있는 조합마다 치킨 거리 구해서 최솟값 갱신
    min_chicken_dist = int(1e9)  # 최소 치킨 거리, 최댓값으로 초기값 설정
    for alive_stores in combinations(stores, m):
        # 각 집마다 가장 가까운 치킨집의 거리 구하고, 치킨 거리에 합산하기
        chicken_dist = 0  # 현재 조합에 대한 치킨 거리
        for house in houses:
            min_dist = int(1e9)  # 집-치킨집 최소 거리, 최댓값으로 초기값 설정
            for store in alive_stores:
                min_dist = min(min_dist, abs(house[0] - store[0]) + abs(house[1] - store[1]))
            chicken_dist += min_dist
        min_chicken_dist = min(min_chicken_dist, chicken_dist)

    print(min_chicken_dist)


solution()
