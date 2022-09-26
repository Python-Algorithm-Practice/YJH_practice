"""
BOJ 11404 플로이드
"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    m = int(sys_input())

    graph = [[int(1e9)] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for _ in range(m):
        begin, end, dist = map(int, sys_input().split())
        graph[begin - 1][end - 1] = min(graph[begin - 1][end - 1], dist)

    for via in range(n):
        for begin in range(n):
            for end in range(n):
                graph[begin][end] = min(graph[begin][end],
                                        graph[begin][via] + graph[via][end])

    for i in range(n):
        for j in range(n):
            print(graph[i][j] if graph[i][j] != int(1e9) else 0, end=' ')
        print()


solution()
