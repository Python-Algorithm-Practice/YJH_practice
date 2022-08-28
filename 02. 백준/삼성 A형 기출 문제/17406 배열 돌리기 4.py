"""

"""
import sys


def next_permutation(rotate_order, key):  # 입력 받은 키를 기준으로 순열 탐색
    # key: (행 * (열의 길이) + 열) * 100 + s -> (1 ~ N - 2) 자리는 1차원 배열 인덱스 / (N - 1 ~ N) 자리는 s
    # 행 * (열의 길이) + 열 -> 1차원 배열로 변환했을 때 인덱스 / 5 X 6 배열의 (2, 3) 원소의 경우 2 * 6 + 3 = 15
    # * 100 + s -> s가 최대 24까지 나올 수 있으므로 그대로 들어가게 하기 위해 * 100
    # 5 X 6 배열, (2, 3, 12)를 입력 받았을 경우 key: (2 * 6 + 3) * 100 + 12 = 1512
    i = len(rotate_order) - 1
    while i > 0 and key(rotate_order[i - 1]) >= key(rotate_order[i]):
        i -= 1

    if i == 0:
        return False

    j = len(rotate_order) - 1
    while key(rotate_order[i - 1]) >= key(rotate_order[j]):
        j -= 1

    rotate_order[i - 1], rotate_order[j] = rotate_order[j], rotate_order[i - 1]

    j = len(rotate_order) - 1
    while i < j:
        rotate_order[i], rotate_order[j] = rotate_order[j], rotate_order[i]
        i += 1
        j -= 1

    return True


def rotate(nums, begin, end):
    """
    :param nums: 배열
    :param begin: 회전할 구역의 시작점 (좌측 상단)
    :param end: 회전할 구역의 끝점 (우측 하단)
    :return: None
    """
    begin_r, begin_c = begin
    end_r, end_c = end

    save = nums[begin_r][begin_c]  # 초기값

    for row in range(begin_r, end_r):  # 사각형의 좌측을 따라 덮어 씌우기
        nums[row][begin_c] = nums[row + 1][begin_c]
    for col in range(begin_c, end_c):  # 사각형의 하단을 따라 덮어 씌우기
        nums[end_r][col] = nums[end_r][col + 1]
    for row in range(end_r, begin_r, -1):  # 사각형의 우측을 따라 덮어 씌우기
        nums[row][end_c] = nums[row - 1][end_c]
    for col in range(end_c, begin_c, -1):  # 사각형의 상단을 따라 덮어 씌우기
        nums[begin_r][col] = nums[begin_r][col - 1]

    nums[begin_r][begin_c + 1] = save  # 덮어 씌워져 사라진 초기값 대입


def solution():
    sys_input = sys.stdin.readline

    n, m, k = map(int, sys_input().split())
    nums = [list(map(int, sys_input().split())) for _ in range(n)]
    
    # 회전 순서 입력
    rotate_orders = []
    for _ in range(k):
        r, c, s = map(int, sys_input().split())
        rotate_orders.append([r - 1, c - 1, s])  # 인덱스 0 기준으로 맞추기
    rotate_orders.sort(key=lambda x: (x[0] * m + x[1]) * 100 + x[2])  # 정렬 기준: 1. 행 2. 열 3. S -> 각각 오름차순

    answer = int(1e9)  # 초기값 설정
    while True:
        nums_copy = [num.copy() for num in nums]
        for row, col, s in rotate_orders:
            for dist in range(s, 0, -1):
                rotate(nums_copy, (row - dist, col - dist), (row + dist, col + dist))
        answer = min(answer, min(sum(line) for line in nums_copy))
        # do - while
        if next_permutation(rotate_orders, lambda x: (x[0] * m + x[1]) * 100 + x[2]):
            continue
        break

    print(answer)


solution()
