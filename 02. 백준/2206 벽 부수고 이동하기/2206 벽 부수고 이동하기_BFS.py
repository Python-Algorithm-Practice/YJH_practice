"""
BFS 두 번 돌리기
BFS 1. 시작점에서 BFS를 돌려 [(만나는 벽의 위치, 시작점으로부터의 최단거리), ...], 도착점까지의 거리 구하기
BFS 2. 모든 지점을 다시 최댓값으로 초기화 하고, 1번에서 구한 벽들의 위치부터 다시 BFS를 돌리며 도착점까지의 최단거리 갱신
"""
import sys
from collections import deque


def first_bfs(board):
    # 방문 배열
    #   elem == int(1e9) -> 미방문
    #   elem < int(1e9) -> 방문
    visit = [[int(1e9)] * len(board[0]) for _ in range(len(board))]
    visit[0][0] = 1  # 시작점 초기화

    bfs_q = deque([(0, 0)])  # BFS 시작점 설정
    walls = []  # 벽의 정보 (벽의 위치, 시작점으로부터 최단거리)

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 좌표 이동량
    
    # 길(0)을 따라 탐색하면서 각 지점의 최단거리 갱신
    # 벽(1)을 만나게 되면, 해당 벽은 첫 번째로 만나는 벽, 즉 부술 수 있는 벽이므로 walls 배열에 정보 저장
    while bfs_q:
        r, c = bfs_q.popleft()

        for direc in range(4):
            next_r, next_c = r + dx[direc], c + dy[direc]  # 다음 좌표
            # 다음 좌표가 유효하고 아직 미방문 상태라면,
            if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]) \
                    and visit[next_r][next_c] == int(1e9):
                visit[next_r][next_c] = visit[r][c] + 1  # 최단거리 갱신
                if board[next_r][next_c] == '0':  # 길이면 BFS 큐에 추가
                    bfs_q.append((next_r, next_c))
                else:  # 벽이라면 부술 수 있는 벽 리스트인 walls에 추가
                    walls.append((next_r, next_c, visit[next_r][next_c]))

    return walls, visit[-1][-1]  # 부술 수 있는 벽들의 정보와 도착점까지의 최단거리 반환


def second_bfs(board, walls, min_dist):
    bfs_q = deque()
    visit = [[int(1e9)] * len(board[0]) for _ in range(len(board))]
    visit[-1][-1] = min_dist
    for r, c, dist in walls:
        visit[r][c] = dist
        bfs_q.append((r, c))

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 좌표 이동량

    # first_bfs()에서 얻은 벽들의 정보 활용하여 다시 BFS 탐색
    # 해당 벽들을 모두 부수었다고 가정하고, 각 지점들부터 BFS 시작
    # 길(0)을 따라 BFS 진행,
    # 단 최단거리가 갱신된 지점의 경우, 해당 지점의 인접점의 최단거리 역시 갱신될 수 있으므로 이미 방문을 했더라도 큐에 재삽입
    while bfs_q:
        r, c = bfs_q.popleft()

        for direc in range(4):
            next_r, next_c = r + dx[direc], c + dy[direc]  # 다음 좌표
            # 다음 좌표가 유효하고 길이라면,
            if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]) \
                    and board[next_r][next_c] == '0':
                # 최단거리를 단축시킬 수 있다면, 최단거리를 갱신하고 해당 지점을 큐에 재삽입
                if visit[next_r][next_c] > visit[r][c] + 1:
                    visit[next_r][next_c] = visit[r][c] + 1
                    bfs_q.append((next_r, next_c))

    # 도착점에 도달할 수 없는 경우 -1 반환
    if visit[-1][-1] == int(1e9):
        return -1
    return visit[-1][-1]


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    board = [list(sys_input().rstrip()) for _ in range(n)]

    walls, min_dist = first_bfs(board)
    print(second_bfs(board, walls, min_dist))


solution()
