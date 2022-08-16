"""

"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n, k = map(int, sys_input().split())
    arr_a = sorted(list(map(int, sys_input().split())))
    arr_b = sorted(list(map(int, sys_input().split())), reverse=True)

    for i in range(k):
        if arr_a[i] >= arr_b[i]:
            break
        arr_a[i], arr_b[i] = arr_b[i], arr_a[i]

    print(sum(arr_a))


solution()
