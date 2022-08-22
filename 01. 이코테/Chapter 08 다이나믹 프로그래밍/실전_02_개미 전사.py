"""

"""
import sys


def comb(nums, idx, n, memo):
    if idx >= n:
        return 0
    if memo[idx]:
        return memo[idx]

    max_val = max(
        comb(nums, idx + 1, n, memo),  # 현재 값을 안 더했을 때,
        comb(nums, idx + 2, n, memo) + nums[idx]  # 현재 값을 더했을 때,
    )

    memo[idx] = max_val
    return max_val


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    nums = list(map(int, sys_input().split()))
    print(comb(nums, 0, n, [0] * n))


solution()
