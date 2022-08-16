"""

"""


def binary_search(nums, find):
    begin, end = 0, len(nums) - 1

    while begin < end:
        mid = (begin + end) >> 1

        if nums[mid] == find:
            return find
        elif nums[mid] < find:
            begin = mid + 1
        else:
            end = mid

    return -1


n = 10000
nums = [i for i in range(1, n + 1)]

print(binary_search(nums, 9921))
