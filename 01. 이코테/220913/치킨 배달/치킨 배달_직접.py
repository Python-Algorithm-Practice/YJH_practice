"""
BOJ 15686 https://www.acmicpc.net/problem/15686
직접 조합 구하기 (약ㄱㄱㄱㄱㄱㄱ간 더 빠른 듯)
"""
import sys


def combinations(stores, idx, m, houses, alive_stores=[]):
    if len(alive_stores) == m:
        chicken_dist = 0
        for house in houses:
            min_dist = int(1e9)
            for store in alive_stores:
                min_dist = min(min_dist, abs(house[0] - store[0]) + abs(house[1] - store[1]))
            chicken_dist += min_dist
        return chicken_dist

    min_chicken_dist = int(1e9)

    for i in range(idx, len(stores)):
        alive_stores.append(stores[i])
        min_chicken_dist = min(min_chicken_dist, combinations(stores, i + 1, m, houses, alive_stores))
        alive_stores.pop()

    return min_chicken_dist


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

    print(combinations(stores, 0, m, houses))


solution()
