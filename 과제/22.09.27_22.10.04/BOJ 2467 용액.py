"""
투 포인터 사용, O(N)

왜?
    1. 최대한 특정 값에 가깝게 맞추어야 함
    2. 정렬이 되어 있다면 아래 알고리즘으로 일반화 가능
        1) 최소 커서, 최대 커서 등 두 개의 포인터 설정
        2) 커서가 가리키는 값들을 더하고 아래와 같이 분기를 나누어 진행
            2.1) 더한 값이 특정 값보다 작다면, 값을 키워야 하므로 최소 커서를 증가
            2.2) 더한 값이 특정 값보다 크다면, 값을 줄여야 하므로 최대 커서를 감소
        3) 최소 커서와 최대 커서가 교차할 때까지 반복
"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    nums = list(map(int, sys_input().split()))

    # 최솟값, 최솟값일 때 왼쪽 커서의 값과 오른쪽 커서의 값
    min_value = abs(nums[0] + nums[-1])
    min_left, min_right = 0, n - 1

    left_cursor, right_cursor = 0, n - 1  # 최소 커서, 최대 커서 설정
    while left_cursor < right_cursor:  # 두 커서가 교차할 때까지,
        value = nums[left_cursor] + nums[right_cursor]  # 값을 더하고
        if abs(value) < min_value:  # 최솟값 확인 및 갱신
            min_value = abs(value)
            min_left = left_cursor
            min_right = right_cursor
        if value < 0:  # 값이 음수라면 값을 키워야 하므로 최소 커서 증가
            left_cursor += 1
        else:  # 값이 양수라면 값을 낮춰야 하므로 최대 커서 감소
            right_cursor -= 1

    print(nums[min_left], nums[min_right])


solution()