"""
LIS, O(NlogN)
"""
import sys


def find_position(lis, num):
    begin, end = 0, len(lis) - 1
    while begin < end:
        mid = (begin + end) >> 1
        if lis[mid] > num:
            begin = mid + 1
        elif lis[mid] < num:
            end = mid
        else:
            return mid
    return begin


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    nums = list(map(int, sys_input().split()))

    lis = [nums[0]]
    for i in range(1, len(nums)):
        if lis[-1] > nums[i]:  # LIS 를 최대한 연장할 수 있으면 연장
            lis.append(nums[i])
        else:  # nums[i]로 대체할 수 있는 공간을 찾아서 삽입
            lis[find_position(lis, nums[i])] = nums[i]
    print(n - len(lis))


solution()
