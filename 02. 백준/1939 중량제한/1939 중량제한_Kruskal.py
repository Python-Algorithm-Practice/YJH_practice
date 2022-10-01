"""
크루스칼
1. 중량 내림차순으로 간선 정렬
2. 가장 큰 것부터 차례로 선택하여 그래프 생성
3. 중량이 w인 간선을 선택했을 때 begin, end 노드가 연결되면 w 반환
4. 속도, 메모리: Kruskal > BFS > DFS
"""
import sys


def find_root(roots, num):
    if roots[num] != num:
        roots[num] = find_root(roots, roots[num])
    return roots[num]


def kruskal(edges, n, begin, end):
    edges.sort(reverse=True)  # w, a, b 기준 내림차순 정렬

    roots = [i for i in range(n + 1)]

    for w, a, b in edges:
        root_a = find_root(roots, a)
        root_b = find_root(roots, b)
        if root_a != root_b:
            roots[root_a] = root_b
            if find_root(roots, begin) == find_root(roots, end):
                return w

    return -1


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())

    edges = []  # 간선 리스트
    for _ in range(m):
        a, b, w = map(int, sys_input().split())
        edges.append((w, a, b))  # w 기준으로 정렬해야 하므로 w를 가장 앞으로
    begin, end = map(int, sys_input().split())

    print(kruskal(edges, n, begin, end))


# 1 -> 4
# [((1, 2), 12), ((1, 3), 10), ((2, 4), 4)]
# root: [1, 1, 1, 1]

solution()
