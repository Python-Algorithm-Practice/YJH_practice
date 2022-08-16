"""

"""
import sys


def binary_search(nums, find):
    begin, end = 0, len(nums) - 1

    while begin < end:
        mid = (begin + end) >> 1

        if nums[mid] == find:
            return 'yes'
        elif nums[mid] < find:
            begin = mid + 1
        else:
            end = mid

    return 'no' if nums[begin] != find else 'yes'


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    list_n = sorted(list(map(int, sys_input().split())))

    m = int(sys_input())
    list_m = list(map(int, sys_input().split()))

    answer = [binary_search(list_n, find) for find in list_m]
    print(*answer)


solution()
