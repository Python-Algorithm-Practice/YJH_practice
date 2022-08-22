"""
BOJ 1516 게임 개발
"""
import sys
from collections import deque


class Building:
    def __init__(self):
        self.total_time = 0
        self.build_time = 0
        self.next_buildings = []
        self.degree_in = 0


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    buildings = [Building() for _ in range(n)]
    for idx in range(n):
        info = list(map(int, sys_input().split()))
        buildings[idx].build_time = info[0]  # 건설 시간
        buildings[idx].degree_in = len(info) - 2  # 진입 차수 설정 (사전에 필요한 건물 개수)
        for next_building in info[1:-1]:
            buildings[next_building - 1].next_buildings.append(idx)  # 다음 건물로 설정

    # 진입 차수가 0인, 조건 없이 지을 수 있는 건물 짓기
    bfs_q = deque()
    for idx in range(n):
        if buildings[idx].degree_in == 0:
            bfs_q.append(idx)  # 건설 목록에 추가
            buildings[idx].total_time = buildings[idx].build_time  # 가장 처음에 지어지므로 완성되기까지 전체 시간 초기화

    while bfs_q:
        front = bfs_q.popleft()  # 건물 짓기

        for next_building in buildings[front].next_buildings:
            buildings[next_building].degree_in -= 1  # 해당 건물을 짓기 위한 조건을 하나 충족했으므로 진입 차수 감소
            # 해당 건물을 짓기까지 소모되는 시간 갱신
            buildings[next_building].total_time = max(
                buildings[next_building].total_time,
                buildings[front].total_time + buildings[next_building].build_time
            )
            if buildings[next_building].degree_in == 0:
                bfs_q.append(next_building)  # 건물을 지을 수 있으므로 큐에 삽입

    for building in buildings:
        print(building.total_time)


solution()
