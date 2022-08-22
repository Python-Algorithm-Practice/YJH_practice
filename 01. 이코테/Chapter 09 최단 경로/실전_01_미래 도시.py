"""
1번에 대해 다익스트라 + K번에 대해 다익스트라
or
속 편하게 플로이드 워셜
"""
import sys
import heapq


def dijkstra(graph, begin, destination):
    distance_to = [int(1e9)] * len(graph)
    distance_to[begin] = 0

    dijk_q = [(0, begin)]

    while dijk_q:
        dist, cur = heapq.heappop(dijk_q)
        if distance_to[cur] < dist:
            continue

        for next_node in graph[cur]:
            if distance_to[next_node] > dist + 1:
                distance_to[next_node] = dist + 1
                heapq.heappush(dijk_q, (dist + 1, next_node))

    return distance_to[destination]


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        begin, end = map(int, sys_input().split())
        graph[begin].append(end)
        graph[end].append(begin)
    x, k = map(int, sys_input().split())

    print(dijkstra(graph, 1, k) + dijkstra(graph, k, x))


solution()
