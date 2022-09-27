"""

"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())

    houses = [0] * 100001
    for house in map(int, sys_input().split()):
        houses[house] += 1

    dist_from_right = 0
    house_cnt_from_right = 0
    for right_cursor in range(100000, 0, -1):
        dist_from_right += house_cnt_from_right
        house_cnt_from_right += houses[right_cursor]

    min_dist = int(2e10)
    min_house = 0

    dist_from_left = 0
    house_cnt_from_left = 0
    for cursor in range(1, 100001):
        dist_from_left += house_cnt_from_left
        house_cnt_from_left += houses[cursor]

        if houses[cursor] and min_dist > dist_from_left + dist_from_right:
            min_dist = dist_from_left + dist_from_right
            min_house = cursor

        house_cnt_from_right -= houses[cursor]
        dist_from_right -= house_cnt_from_right

    print(min_house)


solution()
