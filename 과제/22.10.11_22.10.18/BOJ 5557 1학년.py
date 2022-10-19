"""
DP, O(...?)

왜?
    1. 그냥 계산하면 2^100 난리 남
    2. 같은 계산 결과가 계속 사용됨
    3. DP
"""
import sys


def counting(nums, idx, range_check, result, memo):
    """
    nums[idx:] 수를 사용하여 result를 만들 수 있는 경우의 수를 반환

    :param range_check: 중간 계산 결과가 0 이상 20 이하인지 확인하는 용도
    :param result: 만들어야 하는 결과
    :param memo: 3차원 리스트, memo[idx 이후의 수들에 대해][양수 또는 음수인][수]를 만드는 경우의수
    """
    if idx == len(nums):  # 마지막 도달 시 result 달성 여부에 따라 1, 0 반환
        return 1 if result == 0 else 0
    if range_check < 0 or 20 < range_check:  # 0 <= 계산 결과 <= 20 확인
        return 0
    if memo[idx][result < 0][abs(result)] != -1:  # nums[idx:]로 result를 만들 수 있는 경우를 이미 구했다면 바로 반환
        return memo[idx][result < 0][abs(result)]

    count = 0
    count += counting(nums, idx + 1, range_check + nums[idx], result - nums[idx], memo)  # 더했을 경우, result - nums[idx]를 만들어야 함
    count += counting(nums, idx + 1, range_check - nums[idx], result + nums[idx], memo)  # 뺐을 경우, result + nums[idx]를 만들어야 함
    memo[idx][result < 0][abs(result)] = count

    return count


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    *nums, result = map(int, sys_input().split())
    memo = [[[-1] * 21 for _ in range(2)] for _ in range(n + 1)]
    print(counting(nums, 1, nums[0], result - nums[0], memo))  # 맨앞의 수는 항상 양수이므로 고정 후 인덱스 1부터 시작


solution()
