"""
1. 비트마스크로 행, 열, 블록 방문 기록
2. (i, j) 위치에서 행[i], 열[j], 블록[i // 3][j // 3]을 or 연산했을 때, 0인 비트만 방문해야 함
    Ex) 행[i]     1 0000 1111
        열[j]     0 1101 0110
        블록[i][j] 1 1001 0100
        => (i, j) 올 수 있는 원소 : 1 1101 1111 (6번째 비트가 0이므로 숫자 6)
"""
import sys


def get_sudoku(board, empty_loc, idx, row_visit, col_visit, block_visit):
    if idx == len(empty_loc):
        return True

    row, col = empty_loc[idx]  # 빈 좌표
    visit = row_visit[row] | col_visit[col] | block_visit[row // 3][col // 3]  # 현재 좌표에서 방문 상태

    for i in range(9):
        visit_bit = 1 << i
        if (visit & visit_bit) == 0:
            board[row][col] = i + 1
            row_visit[row] |= visit_bit
            col_visit[col] |= visit_bit
            block_visit[row // 3][col // 3] |= visit_bit

            # 스도쿠 구했으면 바로 종료
            if get_sudoku(board, empty_loc, idx + 1, row_visit, col_visit, block_visit):
                return True

            board[row][col] = 0
            row_visit[row] &= ~visit_bit
            col_visit[col] &= ~visit_bit
            block_visit[row // 3][col // 3] &= ~visit_bit

    # 여기까지 도달 시 스도쿠를 구하지 못 한 것이므로 False 반환
    return False


def solution():
    sys_input = sys.stdin.readline

    board = [list(map(int, sys_input().split())) for _ in range(9)]

    # 방문 기록 리스트
    row_visit = [0] * 9  # 행 방문 기록
    col_visit = [0] * 9  # 열 방문 기록
    block_visit = [[0] * 3 for _ in range(3)]  # 블록 방문 기록

    # 방문 처리 및 채워야 하는 위치 파악
    empty_loc = []
    for row in range(9):
        for col in range(9):
            if board[row][col]:  # 어떤 숫자로 차있다면 방문 기록
                visit_bit = 1 << (board[row][col] - 1)
                row_visit[row] |= visit_bit
                col_visit[col] |= visit_bit
                block_visit[row // 3][col // 3] |= visit_bit
            else:
                empty_loc.append((row, col))

    get_sudoku(board, empty_loc, 0, row_visit, col_visit, block_visit)

    for row in board:
        print(*row)


solution()
