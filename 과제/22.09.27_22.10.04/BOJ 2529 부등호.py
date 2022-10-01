"""
DFS, 완전탐색, 백트래킹 (가지치기), O(N!)..?

왜?
    1. 위치와 부등호의 종류에 따라 각 자리에 들어갈 수 있는 수가 다양함
    2. 들어갈 수 있는 수가 0 ~ 9로 굉장히 한정적임
    3. 따라서 최대 10!이므로 완전탐색 시도

백트래킹 (가지치기) 기준
    1. 부등호가 '마지막 숫자 >' 라면, 마지막 숫자보다 작은 수들을 재귀 호출
        1) 최댓값 출력의 경우
            마지막 숫자 - 1부터 0까지 1씩 감소해 내려가면서 재귀 호출
        2) 최솟값 출력의 경우
            0부터 마지막 숫자 - 1까지 1씩 증가해 올라가면서 재귀 호출

    2. 부등호가 '마지막 숫자 <' 라면, 마지막 숫자보다 큰 수들을 재귀 호출
        1) 최댓값 출력의 경우
            9부터 마지막 숫자 + 1까지 1씩 감소해 내려가면서 재귀 호출
        2) 마지막 숫자 + 1부터 9까지 1씩 증가해 올라가면서 재귀 호출
"""
import sys


def dfs(nums, signs, sign_idx, visit, cmp):
    if len(signs) == sign_idx:  # 모든 부등호를 처리했다면 유효한 명제이므로 출력 후 참 반환
        print(''.join(map(str, nums)))
        return True

    # 최댓값, 최솟값 출력에 따라 반복 range를 다르게 설정
    if cmp == 'MAX':
        loop_range = range(nums[-1] - 1, -1, -1) if signs[sign_idx] == '>' else range(9, nums[-1], -1)
    else:  # MIN
        loop_range = range(nums[-1]) if signs[sign_idx] == '>' else range(nums[-1] + 1, 10)

    # 위에서 설정한 range에 맞게 반복
    for i in loop_range:
        visit_bit = 1 << i  # 방문 체크용 비트
        if visit & visit_bit == 0:  # 미방문일 경우, 해당 숫자를 추가한 뒤 재귀 호출
            nums.append(i)
            if dfs(nums, signs, sign_idx + 1, visit | visit_bit, cmp):  # 유효한 조합을 찾았다면 바로 반환
                return True
            nums.pop()

    return False


def solution():
    sys_input = sys.stdin.readline

    k = int(sys_input())
    signs = sys_input().rstrip().split()

    # 최댓값 출력, 9 ~ 0을 차례로 초기값으로 설정 후 DFS
    for i in range(9, -1, -1):
        if dfs([i], signs, 0, 1 << i, 'MAX'):
            break

    # 최솟값 출력, 0 ~ 9를 차례로 초기값으로 설정 후 DFS
    for i in range(10):
        if dfs([i], signs, 0, 1 << i, 'MIN'):
            break


solution()