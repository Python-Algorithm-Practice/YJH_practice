"""

"""
import sys


def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i == 0:
        return False

    j = len(arr) - 1
    while arr[i - 1] >= arr[j]:
        j -= 1

    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return True


def go_next_base(base_state, count):
    score = 0
    for i in range(3, -1, -1):
        if base_state[i]:
            base_state[i] = False
            if i + count > 3:  # 홈으로 갔을 경우
                score += 1
                continue
            # 진루 처리
            base_state[i + count] = True

    return score


def simulation(perm, innings):
    score = 0  # 총점
    order = 0  # 1번 타자부터 시작

    for inning in innings:
        base_state = [False] * 4  # 타석, 1루, 2루, 3루
        out_count = 0
        score_stk = []
        while out_count < 3:
            base_state[0] = True

            if order < 3:
                cur_order = perm[order]
            elif order == 3:
                cur_order = 0
            else:
                cur_order = perm[order - 1]

            if inning[cur_order] == 0:
                out_count += 1
            else:
                score_stk.append(inning[cur_order])
            order = (order + 1) % 9

        while score_stk:
            if score_stk[-1] > 3:
                score += len(score_stk)
                break
            top = score_stk.pop()
            if score_stk:
                score_stk[-1] += top
    
    return score


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    innings = [list(map(int, sys_input().split())) for _ in range(n)]

    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    max_score = 0
    while next_permutation(arr):
        max_score = max(max_score, simulation(arr, innings))
    print(max_score)


solution()
