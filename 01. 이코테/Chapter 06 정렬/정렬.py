"""

"""
import sys
from time import time
import random


def merge_sort(result, nums, begin, end):
    mid = (begin + end) // 2

    if begin < mid:
        merge_sort(result, nums, begin, mid)
    if mid + 1 < end:
        merge_sort(result, nums, mid + 1, end)

    result_idx = begin
    left, right = begin, mid + 1
    while left <= mid and right <= end:
        if nums[left] < nums[right]:
            result[result_idx] = nums[left]
            left += 1
        else:
            result[result_idx] = nums[right]
            right += 1
        result_idx += 1
    while left <= mid:
        result[result_idx] = nums[left]
        left += 1
        result_idx += 1
    while right <= end:
        result[result_idx] = nums[right]
        right += 1
        result_idx += 1

    for idx in range(begin, end + 1):
        nums[idx] = result[idx]


def quick_sort(nums, begin, end, depth):
    if depth > 0:
        random_pivot = random.randint(begin, end)
        nums[begin], nums[random_pivot] = nums[random_pivot], nums[begin]

        pivot = begin
        left, right = begin + 1, end

        while left <= right:
            while left <= end and nums[pivot] >= nums[left]:
                left += 1
            while begin < right and nums[pivot] <= nums[right]:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        if left > right:
            nums[pivot], nums[right] = nums[right], nums[pivot]

        if begin < right:
            quick_sort(nums, begin, right, depth - 1)
        if right + 1 < end:
            quick_sort(nums, right + 1, end, depth - 1)


def counting_sort(nums):
    max_val = max(nums)

    count = [0] * (max_val + 1)
    for num in nums:
        count[num] += 1

    nums_idx = 0
    for val, cnt in enumerate(count):
        while cnt:
            nums[nums_idx] = val
            nums_idx += 1
            cnt -= 1


def insertion_sort(nums):
    for i in range(len(nums)):
        while 0 < i and nums[i - 1] > nums[i]:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            i -= 1


def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


def is_ordered_by_asc(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            return False
    return True


def solution():
    sys.setrecursionlimit(10000)
    sys.stdin = open('testcase/testcase.txt')
    sys_input = sys.stdin.readline

    n = int(sys_input())
    nums = list(map(int, sys_input().split()))

    print(is_ordered_by_asc(nums))
    begin = time()

    # selection_sort(nums)
    quick_sort(nums, 0, n - 1, 20)
    print(is_ordered_by_asc(nums))
    insertion_sort(nums)
    # counting_sort(nums)
    # merge_sort([0] * n, nums, 0, n - 1)
    # nums.sort()

    print(f'실행시간 : {time() - begin} secs')
    print(is_ordered_by_asc(nums))


solution()
