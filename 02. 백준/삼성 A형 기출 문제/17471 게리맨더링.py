"""

"""
import sys


def dfs(graph, district, num, population):
    """
    :param graph: 구역 간 연결 관계
    :param district: 아직 방문하지 않은 구역
    :param num: 현재 방문중인 구역
    :param population: 구역별 인구수
    :return: 현재 구역의 인구수와 district 구역들의 인구수 합
    """
    pop_sum = population[num]

    for next_sector in graph[num]:
        if next_sector in district:
            district.remove(next_sector)
            pop_sum += dfs(graph, district, next_sector, population)

    return pop_sum


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    populations = list(map(int, sys_input().split()))
    graph = [list(map(lambda x: int(x) - 1, sys_input().split()[1:])) for _ in range(n)]

    min_diff = 1001
    for subset in range(1 << n):
        districts = [set(), set()]
        for i in range(n):
            districts[subset & 1 << i > 0].add(i)

        # 0번 지역구와 1번 지역구의 인구수 차이 구하기
        diff = 0
        diff += dfs(graph, districts[0], districts[0].pop(), populations) if len(districts[0]) > 0 else 0
        diff -= dfs(graph, districts[1], districts[1].pop(), populations) if len(districts[1]) > 0 else 0

        # dfs 했을 때 아직 방문하지 않은 구역이 남아있다면 제대로 나누어진 것이 아님
        if len(districts[0]) == len(districts[1]) == 0:
            min_diff = min(min_diff, abs(diff))

    print(min_diff if min_diff != 1001 else -1)


solution()
