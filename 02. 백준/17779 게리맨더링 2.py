"""
음...
"""
import sys


def count_all(board, row, col, total):
    min_diff = int(1e9)

    for d1 in range(1, col + 1):
        if row + d1 >= len(board):  # 5번 구역의 크기가 전체 구역을 벗어날 경우 탐색 종료
            break
        for d2 in range(1, len(board) - col):
            if row + d1 + d2 >= len(board):  # 구역 유효 여부 판단
                break
            # 상좌우하 꼭짓점 좌표
            up = row, col
            left = row + d1, col - d1
            right = row + d2, col + d2
            down = right[0] + d1, right[1] - d1

            population = [0, 0, 0, 0, 0]  # 구역별 인구수 5, 1 ~ 4번
            for r in range(len(board)):
                if r < left[0]:  # 1번, 왼쪽 꼭짓점 행보다 작아야 함
                    population[1] += board[r][min(up[1], up[1] - r + up[0] - 1)]
                else:  # 3번, 왼쪽 꼭짓점 행보다 크거나 같아야 함
                    col_3 = min(left[1] + r - left[0] - 1, down[1] - 1)
                    if col_3 >= 0:
                        population[3] += board[r][col_3]

                if r <= right[0]:  # 2번, 오른쪽 꼭짓점 행보다 작거나 같아야 함
                    population[2] += board[r][-1] - board[r][max(up[1], up[1] + r - up[0])]
                else:  # 4번, 오른쪽 꼭짓점 행보다 커야 함
                    population[4] += board[r][-1] - board[r][max(right[1] - (r - right[0]), down[1] - 1)]

            population[0] = total - sum(population)  # 5번 영역의 인구수
            population.sort()  # 최대 최소를 구하기 위해 정렬
            min_diff = min(min_diff, population[-1] - population[0])  # 최소 차이 갱신

    return min_diff


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    board = [list(map(int, sys_input().split())) for _ in range(n)]
    for row in board:  # board -> 누적합 배열로 변환 -> 이유? 경우의 수마다 똑같은 수를 계속 더해야 하므로 중복 연산을 줄이기 위해
        for i in range(1, n):
            row[i] += row[i - 1]

    total = sum([row[-1] for row in board])  # 총 인구수
    min_diff = int(1e9)  # 초기값으로 INF 설정
    for i in range(n - 2):  # N - 2, N - 1번째 행은 5번 구역의 시작점이 될 수 없음
        for j in range(1, n - 1):  # 0, N - 1번째 열은 5번 구역의 시작점이 될 수 없음
            min_diff = min(min_diff, count_all(board, i, j, total))

    print(min_diff)


solution()
