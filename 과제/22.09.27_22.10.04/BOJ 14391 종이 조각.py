"""
브루트포스, O(......?)

왜?
    1. 데이터 제한이 굉장히 낮아서 완탐 생각
    2. 어떻게 종이 조각을 자르는지에 따라 값이 달라지므로
"""
import sys


def get_unvisited(visit):
    """
    :param visit: 방문 여부 배열
    :return: 방문해야 할 위치 (행, 열 오름차순 순서로), 방문할 곳이 없다면 None
    """
    for i in range(len(visit)):
        for j in range(len(visit[i])):
            if not visit[i][j]:
                return i, j
    return None


def rCounting(board, visit, total):
    """
    현재 미방문한 곳들에 대해 최댓값을 구하는 함수
    1. 방문할 지점 찾기
    2. 현재 위치를 (r, c)라고 할 때,
        1) (r, c) -> 현재 위치의 조각만 사용했을 때
        2) (r, c) ~ (r, c + i) 까지 조각을 붙였을 때 (행)
        3) (r, c) ~ (r + i, c) 까지 조각을 붙였을 때 (열)
        => 위와 같이 분기를 나누어 합을 구한 뒤, 나머지 미방문한 곳들의 최댓값을 구하기 위해 재귀 호출
    """
    cur_point = get_unvisited(visit)
    if not cur_point:  # 방문할 곳이 없다면 모든 종이 조각을 사용한 것이므로 현재까지 쌓아온 값 반환
        return total
    r, c = cur_point
    max_total = 0

    # (r, c) ~ (r, c + i) (i >= 0) 조각을 이어 붙인 뒤 각각의 경우 대해 최댓값 구하기
    col_idx = c
    value = 0
    while col_idx < len(board[0]) and not visit[r][col_idx]:
        visit[r][col_idx] = True  # 현재 사용할 조각 방문 처리
        # (r, c) 조각부터 (r, col_idx)까지 이어 붙인 조각의 값 갱신
        value = value * 10 + board[r][col_idx]  # 자릿수 증가 및 일의 자리 더하기
        # total + value를 넘겨주고 미방문 위치들에 대한 최댓값을 구해와 갱신하기
        max_total = max(max_total, rCounting(board, visit, total + value))
        # 다음 종이 조각 이어 붙이러~
        col_idx += 1
    for i in range(c, col_idx):  # 다음 경우를 세기 위해 방문 처리 해제
        visit[r][i] = False

    # c열의 각 행에 대해서 똑같이 이어 붙이며 최댓값 구하기
    visit[r][c] = True  # 현재 위치 (r, c)는 이미 위에서 고려했으므로 그냥 방문 처리
    row_idx = r + 1  # 따라서 위치도 (r + 1, c) ~ (r + i, c)가 됨
    value = board[r][c]
    while row_idx < len(board) and not visit[row_idx][c]:
        visit[row_idx][c] = True
        value = value * 10 + board[row_idx][c]
        max_total = max(max_total, rCounting(board, visit, total + value))
        row_idx += 1
    for i in range(r, row_idx):
        visit[i][c] = False

    return max_total


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())

    board = [list(map(int, list(sys_input().rstrip()))) for _ in range(n)]
    visit = [[False] * m for _ in range(n)]

    print(rCounting(board, visit, 0))


solution()
