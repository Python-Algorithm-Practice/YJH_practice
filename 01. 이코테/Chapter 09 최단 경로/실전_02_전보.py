"""
다익스트라
"""
import sys
import heapq


def solution():
    sys_input = sys.stdin.readline

    n, m, c = map(int, sys_input().split())

    graph = [dict() for _ in range(n + 1)]
    for _ in range(m):
        begin, end, weight = map(int, sys_input().split())
        if end in graph[begin]:
            graph[begin][end] = min(graph[begin][end], weight)
        else:
            graph[begin][end] = weight

    distance_to = [int(1e9)] * (n + 1)
    distance_to[c] = 0

    dijk_q = [(0, c)]
    while dijk_q:
        dist, cur = heapq.heappop(dijk_q)
        if distance_to[cur] < dist:
            continue

        for next_node in graph[cur]:
            if distance_to[next_node] > dist + graph[cur][next_node]:
                distance_to[next_node] = dist + graph[cur][next_node]
                heapq.heappush(dijk_q, (distance_to[next_node], next_node))

    cities = 0
    max_time = 0
    for i in range(1, n + 1):
        if 1 <= distance_to[i] < int(1e9):
            cities += 1
            max_time = max(max_time, distance_to[i])

    print(cities, max_time)


solution()
