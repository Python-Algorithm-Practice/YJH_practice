"""

"""
import sys


def get_next_idx(board, cur_idx):
    for idx in range(cur_idx, 100):
        row, col = idx // 10, idx % 10
        if board[row] & 1 << col == 0:
            return idx
    return -1


def attachable(board, row, size, bit):
    for i in range(size):
        if board[row] & bit:
            return False
    return True


def mod_paper(board, row, size, bit, paper_counts, is_attach):
    for i in range(size):
        if is_attach == 'Attach':
            board[row] |= bit
            paper_counts[size] -= 1
        else:
            board[row] &= ~bit
            paper_counts[size] += 1


def counting(board, idx, paper_counts):
    row, col = idx // 10, idx % 10

    count = 0

    for size in range(5):
        if size > col or paper_counts[size] == 0:
            break
        bit = 0
        for i in range(size):
            bit |= 1 << col - i

        if attachable(board, row, size, bit):
            mod_paper(board, row, size, bit, paper_counts, 'Attach')

            next_idx = get_next_idx(board, idx)
            if next_idx == -1:
                mod_paper(board, row, size, bit, paper_counts, 'Detach')
                return 1
            count += counting(board, next_idx, paper_counts)

            mod_paper(board, row, size, bit, paper_counts, 'Detach')

    return count


def solution():
    sys_input = sys.stdin.readline

    board = [0] * 10
    for r in range(10):
        for i, ch in enumerate(sys_input().rstrip().split()):
            if ch == '1':
                board[r] |= 1 << i

    count = 0
    next_idx = get_next_idx(board, 0)
    if next_idx:
        count = counting(board, next_idx, [5, 5, 5, 5, 5])
    print(count)


solution()
