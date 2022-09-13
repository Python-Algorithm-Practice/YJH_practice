"""
BOJ 15483 https://www.acmicpc.net/problem/15483
"""
import sys


def solution():
    sys_input = sys.stdin.readline

    a = list(sys_input().rstrip())
    b = list(sys_input().rstrip())

    memo = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for a_idx in range(len(a) + 1):
        memo[a_idx][0] = a_idx
    for b_idx in range(len(b) + 1):
        memo[0][b_idx] = b_idx

    for a_idx in range(1, len(a) + 1):
        for b_idx in range(1, len(b) + 1):
            memo[a_idx][b_idx] = memo[a_idx - 1][b_idx - 1]
            if a[a_idx - 1] != b[b_idx - 1]:
                memo[a_idx][b_idx] = min(
                    memo[a_idx - 1][b_idx - 1],
                    memo[a_idx - 1][b_idx],
                    memo[a_idx][b_idx - 1]) + 1

                if a_idx > 1 and b_idx > 1 and a[a_idx - 2] == b[b_idx - 1] and a[a_idx - 1] == b[b_idx - 2]:
                    memo[a_idx][b_idx] = min(memo[a_idx][b_idx], memo[a_idx - 2][b_idx - 2] + 1)
                if a_idx > 1 and b_idx > 2 and a[a_idx - 2] == b[b_idx - 1] and a[a_idx - 1] == b[b_idx - 3]:
                    memo[a_idx][b_idx] = min(memo[a_idx][b_idx], memo[a_idx - 2][b_idx - 3] + 2)

    print(memo[len(a)][len(b)])


solution()
