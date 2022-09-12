"""
이분 탐색 + DFS
1. 이분 탐색 기준 : 중량
2. 이분 탐색 내용 : 중량을 W로 설정했을 때 도착지까지 이동할 수 있는지
                    이동할 수 있다면 더 높은 중량에서도 가능한지 확인
                    이동할 수 없다면 중량을 낮추어서 다시 진행
3. 속도, 메모리: Kruskal > BFS > DFS
"""
import sys


def movable_dfs(graph, cur_node, dest_node, visit, min_weight):
    if cur_node == dest_node:
        return True

    visit[cur_node] = True  # 방문 기록

    for next_node, weight in graph[cur_node]:
        if min_weight <= weight and not visit[next_node]:
            # 목적지 도달 시 True 반환하여 바로 종료
            if movable_dfs(graph, next_node, dest_node, visit, min_weight):
                return True

    # 목적지 도달 실패
    return False


def binary_search(graph, begin, end, min_w, max_w):
    answer = min_w
    while min_w < max_w:
        weight = (min_w + max_w) >> 1
        # weight 중량으로 목적지 도달 가능하면 최대 중량 제한 갱신 및 중량 제한 올리기
        if movable_dfs(graph, begin, end, [False] * len(graph), weight):
            answer = weight
            min_w = weight + 1
        else:  # 도달 불가능할 시 중량 제한 낮추기
            max_w = weight
    # min_w, max_w 같아졌을 경우 해당 중량에서 확인
    if min_w == max_w and movable_dfs(graph, begin, end, [False] * len(graph), min_w):
        answer = min_w

    return answer


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())

    graph = [[] for _ in range(n + 1)]  # 인접 리스트
    min_w, max_w = int(1e9), 0  # 이분 탐색의 최소 및 최대 범위
    for _ in range(m):
        a, b, w = map(int, sys_input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
        min_w, max_w = min(min_w, w), max(max_w, w)  # 이분 탐색 범위 갱신
    begin, end = map(int, sys_input().split())

    print(binary_search(graph, begin, end, min_w, max_w))


sys.setrecursionlimit(100000)
solution()
