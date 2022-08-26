"""
0. DFS로 섬마다 번호 할당
1. 가로 및 세로로 탐색하며 edge 구하기
    1) 두 개씩 검사하는데 만약 [섬, 0] 쌍이 등장하면 다른 섬이 등장할 때까지 거리를 세어 나감
    2) 거리를 늘려가다가 다른 섬이 등장하면 edge 생성
    3) 모든 가로와 세로에 대해 적용
2. 크루스칼
"""
import sys


def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def alloc_id(board, r, c, island_id):
    board[r][c] = island_id

    if r > 0 and board[r - 1][c] == 1:
        alloc_id(board, r - 1, c, island_id)
    if c > 0 and board[r][c - 1] == 1:
        alloc_id(board, r, c - 1, island_id)
    if r + 1 < len(board) and board[r + 1][c] == 1:
        alloc_id(board, r + 1, c, island_id)
    if c + 1 < len(board[0]) and board[r][c + 1] == 1:
        alloc_id(board, r, c + 1, island_id)


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    # 0. DFS -> 섬마다 번호 할당 (1번 제외)
    island_id = 2
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                alloc_id(board, i, j, island_id)
                island_id += 1

    # 1. 간선 구하기
    edge_list = []
    for i in range(n):  # 모든 열에 대해 edge 구하기
        idx = 1
        while idx < m:
            if board[i][idx - 1] > 0 and board[i][idx] == 0:  # 섬의 끝자락 발견 시 바다를 건너 다른 섬 찾기
                dist = 0
                while idx < m and board[i][idx] == 0:  # 다른 섬 찾기
                    idx += 1
                    dist += 1
                if idx < m and dist > 1:  # 다른 섬을 찾았고, 2 이상의 다리를 놓을 수 있다면 edge_list 추가
                    edge_list.append((dist, (board[i][idx - dist - 1], board[i][idx])))
            idx += 1

    for i in range(m):  # 모든 행에 대해 edge 구하기
        idx = 1
        while idx < n:
            if board[idx - 1][i] > 0 and board[idx][i] == 0:
                dist = 0
                while idx < n and board[idx][i] == 0:
                    idx += 1
                    dist += 1
                if idx < n and dist > 1:
                    edge_list.append((dist, (board[idx - dist - 1][i], board[idx][i])))
            idx += 1

    edge_list.sort()

    # 2. 크루스칼
    total_length = 0

    parents = [i for i in range(island_id)]  # 섬 개수만큼 루트 리스트 생성

    for dist, edge in edge_list:
        root_a = find_parent(parents, edge[0])
        root_b = find_parent(parents, edge[1])

        if root_a != root_b:
            parents[root_b] = root_a
            total_length += dist

    # 모두 연결됐는지 확인
    for i in range(2, island_id):
        if find_parent(parents, 2) != find_parent(parents, i):
            total_length = -1
            break

    print(total_length)


solution()
