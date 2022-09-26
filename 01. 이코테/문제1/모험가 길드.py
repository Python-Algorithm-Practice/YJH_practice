"""

"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    fears = [0] * (n + 1)  # 공포도별 인원수 리스트 생성, fears[공포도] = 인원수
    for i in map(int, sys_input().split()):
        fears[i] += 1

    # 그룹을 형성할 수 있는 상태 : X 이하의 공포도를 갖는 인원이 X명 이상일 경우 그룹 형성이 가능
    # 1부터 N까지 누적합을 구해가면서 (누적합: fears[i] += fears[i - 1])
    #   만약 그룹을 형성할 수 있다면 그룹을 바로 형성하고 형성된 인원만큼 excluding_count 증가
    
    groups = 0  # 형성되는 그룹의 수
    excluding_count = 0  # 그룹을 갖게 되어 제외되는 인원
    for i in range(2, n + 1):
        fears[i] += fears[i - 1]  # fears[1] + ... + fears[i] 누적합
        real_count = fears[i] - excluding_count  # 실제 인원 (그룹을 구성할 수 있는 인원, 이미 그룹을 가진 사람은 새로 못 구성하므로)
        groups += real_count // i  # 공포도 i에 대해 형성할 수 있는 만큼 최대한 그룹 생성
        excluding_count += real_count // i * i  # 그룹이 구성되어 제외되는 인원 갱신
        
    print(groups)  # 출력


solution()
# cat
# cta
