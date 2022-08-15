"""

"""
import sys
import heapq


def solution():
    sys_input = sys.stdin.readline

    # 입력
    n = int(sys_input())
    cards_count = [int(sys_input()) for _ in range(n)]
    heapq.heapify(cards_count)  # cards_count 리스트를 최소힙으로 변환

    answer = 0  # 총 비교 횟수를 저장할 변수
    for _ in range(n - 1):
        # 가장 적은 두 묶음의 카드를 합침
        count = heapq.heappop(cards_count) + heapq.heappop(cards_count)
        heapq.heappush(cards_count, count)  # 새로운 카드 묶음이 생겼으므로 힙에 push
        answer += count  # 비교 횟수 반영

    print(answer)  # 출력


solution()
