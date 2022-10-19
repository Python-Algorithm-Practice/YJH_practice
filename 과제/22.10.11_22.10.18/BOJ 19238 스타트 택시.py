"""
BFS, O(N^2 * 2M) = O(N^2 * 2 * N^2) = O(N^4)

왜?
    1. 이동 시 가중치가 없기 때문에 BFS로 충분하다고 생각함
    2. 데이터 제한이 낮아 계속 BFS 돌려도 되겠다고 판단함

알고리즘
    0. 데이터
        departure: 출발지 위치가 담긴 set()
        destination[출발지] = 도착지
    1. 연료가 떨어지거나 모든 출발지를 돌 때까지 BFS
        1) 현재 위치에서 시작하여 출발지 찾기 (출발지 Set에 속한 지점 찾기)
        2) 도착지 찾기 (1번에서 구한 출발지의 도착지로 이동)
        3) 1 ~ 2 반복
"""
import sys
from collections import deque


def bfs(board, r, c, compare):
    """
    compare 기준에 맞는 지점을 찾고, 해당 지점의 위치와 이동거리, 지점 번호 반환
    """
    bfs_q = deque([(r, c)])  # BFS 큐

    # 방문 처리용 배열
    visit = [[False] * len(board) for _ in range(len(board))]
    visit[r][c] = True

    # 좌표 이동량 설정
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    move_count = 0  # 이동거리
    while bfs_q:
        bfs_q = deque(sorted(bfs_q))  # 같은 거리에서 행, 열 오름차순 기준으로 뽑기 위해 정렬
        q_size = len(bfs_q)  # 한 단계씩 멀어지며 조사해야 하므로 한 번 돌 때 큐 크기만큼만 돌아줌
        for _ in range(q_size):
            r, c = bfs_q.popleft()
            if compare((r, c)):  # 설정한 기준에 맞는 원소 찾으면 탐색 종료
                return r, c, move_count
            # 미방문 지점 추가
            for direc in range(4):
                next_r, next_c = r + dr[direc], c + dc[direc]
                if 0 <= next_r < len(board) and 0 <= next_c < len(board) \
                        and not visit[next_r][next_c] and board[next_r][next_c] == 0:
                    visit[next_r][next_c] = True
                    bfs_q.append((next_r, next_c))

        move_count += 1  # 이동거리 증가

    return -1, -1, int(1e9)


def simulation(board, r, c, m, f, departure, destination):

    for _ in range(m):
        r, c, move_count = bfs(board, r, c, lambda x: x in departure)  # 출발지 찾기
        f -= move_count  # 연료 소모 반영
        if f <= 0:  # 연료 다 떨어졌다면 -1 반환
            return -1
        departure.remove((r, c))

        dest_r, dest_c, move_count = bfs(board, r, c, lambda x: x == destination[(r, c)])  # 도착지 찾기
        f -= move_count  # 연료 소모 반영
        if f < 0:  # 연료 다 떨어졌다면 -1 반환
            return -1
        f += move_count << 1  # 이동거리의 두 배 충전
        destination[(r, c)] = None
        r, c = dest_r, dest_c

    return f


def solution():
    sys_input = sys.stdin.readline

    n, m, f = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    # 택시 위치 입력
    r, c = map(lambda x: int(x) - 1, sys_input().split())

    # 출발지, 도착지를 같은 절댓값의 음수와 양수로 설정
    departure = set()
    destination = dict()
    for i in range(1, m + 1):
        r1, c1, r2, c2 = map(lambda x: int(x) - 1, sys_input().split())
        departure.add((r1, c1))
        destination[(r1, c1)] = (r2, c2)

    print(simulation(board, r, c, m, f, departure, destination))


solution()
