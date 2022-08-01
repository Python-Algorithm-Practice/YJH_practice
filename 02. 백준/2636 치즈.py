"""
1. 바깥 부분인 (0, 0) 부터 시작해 BFS 진행하여 가장자리 치즈 파악
2. 1번에서 구한 가장자리에 위치한 치즈의 개수를 저장하고 해당 치즈들을 모두 빈칸으로 변경
3. 1번의 치즈 리스트를 BFS 큐로 사용하며 1번부터 반복
"""
import sys
from collections import deque


# 방문 처리 함수. 인자로 받은 위치가 빈칸이라면 BFS 큐에 추가 / 치즈라면 해당 위치를 빈칸으로 바꾸고 edge_cheese 추가
def visit_to(board, row, col, visit, bfs_q, edge_cheese):
    # 유효하지 않은 위치라면 방문 처리 종료
    if not (0 <= row < len(board) and 0 <= col < len(board[0])):
        return 0

    # 이미 방문한 위치라면 수행 종료
    if visit[row][col]:
        return 0

    visit[row][col] = True  # 방문 처리

    if board[row][col] == 0:  # 빈칸이라면 큐에 추가
        bfs_q.append([row, col])
    else:  # 치즈라면 빈칸으로 바꾸고 edge_cheese 추가
        board[row][col] = 0
        edge_cheese.append([row, col])


def solution():
    sys_input = sys.stdin.readline  # 빠른 input

    n, m = map(int, sys_input().split())  # 판의 크기 입력

    board = [list(map(int, sys_input().split())) for _ in range(n)]  # 판 정보 입력

    time = 0  # 치즈가 모두 녹는 시간
    last_cheese = 0  # 마지막에 녹는 치즈의 개수

    bfs_q = deque([[0, 0]])  # BFS 사용하기 위한 큐. (0, 0)은 항상 바깥이므로 시작점으로 선정

    visit = [[False] * m for _ in range(n)]  # 방문 정보
    visit[0][0] = True  # 시작점 방문 처리

    remain_cheese = sum([row.count(1) for row in board])  # 남은 치즈의 개수
    while remain_cheese > 0:  # 치즈가 모두 녹을 때까지 반복
        edge_cheese = deque()  # 이번에 녹을 치즈의 위치 리스트

        while bfs_q:  # BFS 큐가 빌 때까지 반복
            row, col = bfs_q.popleft()  # 방문할 위치 정보

            visit_to(board, row - 1, col, visit, bfs_q, edge_cheese)  # 상단
            visit_to(board, row, col - 1, visit, bfs_q, edge_cheese)  # 좌측
            visit_to(board, row + 1, col, visit, bfs_q, edge_cheese)  # 하단
            visit_to(board, row, col + 1, visit, bfs_q, edge_cheese)  # 우측

        time += 1  # 시간 경과
        last_cheese = len(edge_cheese)  # 녹은 치즈의 개수 갱신

        remain_cheese -= last_cheese  # 남은 치즈의 개수 감소

        bfs_q = edge_cheese  # 현재 녹은 치즈들의 위치부터 BFS 재탐색

    print(time)  # 치즈가 모두 녹은 시간 출력
    print(last_cheese)  # 마지막에 녹은 치즈의 개수 출력


solution()
