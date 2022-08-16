"""

"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n, c = map(int, sys_input().split())
    houses = sorted([int(sys_input()) for _ in range(n)])

    max_diff = 0

    begin = 0
    end = houses[-1] - houses[0]  # 최대 간격은 (가장 먼 공유기 위치 - 가장 가까운 공유기 위치)를 넘을 수 없음

    # 공유기 간격에 대해 이분 탐색
    while begin <= end:
        diff = (begin + end) >> 1  # 공유기 간격

        # 첫 번째 공유기부터 시작하여 diff 간격 이상으로 공유기 배치
        count = 1
        last_router = houses[0]
        for i in range(1, n):
            if houses[i] - last_router >= diff:
                last_router = houses[i]
                count += 1

                if count == c:  # 큰 차이 없음 ㅠ
                    break

        # 공유기를 모두 배치하지 못 했다면 최소 간격을 줄여야 함
        if count < c:
            end = diff - 1
        # 공유기를 c 이상 배치했다면 최소 간격을 늘려볼 수 있음
        else:
            begin = diff + 1
            max_diff = diff  # 최소 간격 중 최댓값 갱신

    print(max_diff)


solution()
