"""
BOJ 1753 최단경로
"""
import sys
import heapq


def solution():
    sys_input = sys.stdin.readline

    v, e = map(int, sys_input().split())
    s = int(sys_input())
    graph = [{} for _ in range(v + 1)]

    for _ in range(e):
        begin, end, weight = map(int, sys_input().split())
        if end in graph[begin]:
            graph[begin][end] = min(graph[begin][end], weight)
        else:
            graph[begin][end] = weight

    distance_to = [int(1e9)] * (v + 1)
    distance_to[s] = 0
    dijk_q = [(0, s)]
    while dijk_q:
        dist, cur = heapq.heappop(dijk_q)
        if distance_to[cur] < dist:
            continue

        for next_node in graph[cur]:
            if distance_to[next_node] > dist + graph[cur][next_node]:
                distance_to[next_node] = dist + graph[cur][next_node]
                heapq.heappush(dijk_q, (distance_to[next_node], next_node))

    for i in range(1, v + 1):
        print(distance_to[i] if distance_to[i] != int(1e9) else 'INF')


solution()
