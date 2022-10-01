"""

"""
import sys


def result(graph, paths):
    adj_set = {paths[0]} | {adj for adj in range(len(graph)) if graph[paths[0]][adj]}

    for p_idx in range(1, len(paths)):
        if paths[p_idx] not in adj_set:
            return 'NO'
        adj_set |= {paths[p_idx]} | {adj for adj in range(len(graph)) if graph[paths[p_idx]][adj]}

    return 'YES'


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    graph = [list(map(int, sys_input().split())) for _ in range(n)]
    paths = list(map(lambda x: int(x) - 1, sys_input().split()))
    print(result(graph, paths))


solution()
