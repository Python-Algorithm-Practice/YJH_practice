"""
BOJ 14888 https://www.acmicpc.net/problem/14888
"""
import sys


def next_permutations(operators):
    i = len(operators) - 1
    while i and ord(operators[i - 1]) >= ord(operators[i]):
        i -= 1
    if i == 0:
        return False

    j = len(operators) - 1
    while ord(operators[i - 1]) >= ord(operators[j]):
        j -= 1

    operators[i - 1], operators[j] = operators[j], operators[i - 1]

    j = len(operators) - 1
    while i < j:
        operators[i], operators[j] = operators[j], operators[i]
        i += 1
        j -= 1

    return True


def calc(nums, operators):
    val = nums[0]
    for i in range(1, len(nums)):
        oper = operators[i - 1][0]
        if oper == '+':  # +
            val += nums[i]
        elif oper == '-':  # -
            val -= nums[i]
        elif oper == '*':  # *
            val *= nums[i]
        else:  # /
            if val < 0:
                val = abs(val) // nums[i] * -1
            else:
                val //= nums[i]
    return val


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    nums = list(map(int, sys_input().split()))  # 정수 리스트
    op_counts = list(map(int, sys_input().split()))  # 연산자 개수 리스트
    # N-P 돌리기 위해 아스키 코드 값을 기준으로 연산자 개수만큼 리스트 생성 (* < + < - < /)
    operators = ['*'] * op_counts[2] + ['+'] * op_counts[0] + ['-'] * op_counts[1] + ['/'] * op_counts[3]

    max_val = min_val = calc(nums, operators)  # 초기값 설정, 가장 처음 연산자 순서 그대로
    while next_permutations(operators):  # 순열로 얻을 수 있는 모든 조합 계산
        val = calc(nums, operators)
        max_val = max(max_val, val)
        min_val = min(min_val, val)

    print(max_val)
    print(min_val)


solution()
