"""
BOJ 1647 도시 분할 계획
"""
import sys
import heapq


def find_parent(set_num, n):
    if set_num[n] != n:
        set_num[n] = find_parent(set_num, set_num[n])
    return set_num[n]


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())

    set_num = [i for i in range(n + 1)]

    edges = {}
    for _ in range(m):
        a, b, w = map(int, sys_input().split())
        if a > b:
            a, b = b, a

        if (a, b) in edges:
            edges[(a, b)] = min(edges[(a, b)], w)
        else:
            edges[(a, b)] = w

    min_heap = [(edges[edge], edge) for edge in edges]
    heapq.heapify(min_heap)

    set_count = n  # 집합의 개수
    total_cost = 0  # 집을 모두 연결하기 위한 비용
    max_cost = 0  # 집을 모두 연결했을 때 그 중 최대인 길의 비용
    while set_count > 1:  # 집합의 개수가 1, 즉 하나의 마을이 될 때까지 집 연결
        min_cost, min_edge = heapq.heappop(min_heap)

        parent_a = find_parent(set_num, min_edge[0])
        parent_b = find_parent(set_num, min_edge[1])

        if parent_a != parent_b:
            set_num[min(parent_a, parent_b)] = max(parent_a, parent_b)
            total_cost += min_cost
            max_cost = max(max_cost, min_cost)
            set_count -= 1

    print(total_cost - max_cost)  # 최대 가격인 길을 끊어 마을을 두 개로 분할


solution()
