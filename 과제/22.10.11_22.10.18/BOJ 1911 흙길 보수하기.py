"""
투 포인터..?, O(N log N)

왜?
    1. 널빤지를 겹치지 않게 웅덩이를 덮어야 함
    2. 그러기 위해선 겹치는 웅덩이를 하나로 합친 뒤 널빤지를 깔아야 함
    3. 웅덩이를 하나로 합치기 위해선 시작점과 끝점 등 두 개의 변수로 관리해야 함
    4. 따라서 물 웅덩이의 범위에 따라 시작점과 끝점을 관리하고 널빤지를 깔았음
"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n, length = map(int, sys_input().split())
    holes = sorted([list(map(int, sys_input().split())) for _ in range(n)])

    min_count = 0  # 필요한 널빤지의 최소 개수
    begin, end = 0, 0
    for hole_begin, hole_end in holes:
        if end < hole_begin:  # 웅덩이 길이를 연장할 수 없다면 널빤지를 깔고 새로운 범위 찾기
            hole_length = end - begin  # 널빤지를 깔아야 할 웅덩이의 길이
            count = (hole_length + length - 1) // length  # 필요한 널빤지의 개수
            min_count += count  # 널빤지 개수 반영
            begin = max(hole_begin, begin + count * length)  # 현재 웅덩이의 시작점보다 마지막으로 깐 널빤지의 끝점이 더 길 수 있음
            end = hole_end
        else:  # 웅덩이 길이 연장
            end = max(end, hole_end)
    # 마지막으로 계산한 웅덩이가 있다면 계산해줌
    if begin < end:
        hole_length = end - begin
        min_count += (hole_length + length - 1) // length

    print(min_count)


solution()
