"""

"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())  # 회의 수 입력
    # 회의별 시작, 종료시간을 입력 받고, 종료시간을 기준으로 오름차순 정렬
    meetings = [list(map(int, sys_input().split())) for _ in range(n)]
    meetings.sort(key=lambda x: (x[1], x[0]))

    last_time = 0  # 마지막 회의가 끝난 시간
    meeting_count = 0  # 진행된 회의의 수
    for begin, end in meetings:  # 회의 정보를 모두 탐색하는데,
        if last_time <= begin:  # 시작시간이 마지막 회의의 종료시간 이후라면, (현재 회의를 진행할 수 있다면,)
            meeting_count += 1  # 진행된 회의의 수를 증가시키고 마지막 회의가 종료된 시간 갱신
            last_time = end

    print(meeting_count)


solution()
