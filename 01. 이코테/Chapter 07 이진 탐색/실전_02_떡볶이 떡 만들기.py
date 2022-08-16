"""

"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    tteoks = list(map(int, sys_input().split()))

    max_length = 0
    begin, end = 0, max(tteoks)
    while begin <= end:
        mid = (begin + end) >> 1

        total = 0
        for tteok in tteoks:
            if tteok > mid:
                total += tteok - mid

        if total < m:
            end = mid - 1
        else:
            max_length = mid
            begin = mid + 1

    print(max_length)


solution()
