"""
BOJ 11727 바닥공사
"""
import sys


# def counting(idx, n, memo):
#     if idx > n:  # n - 1칸에서 2칸 뛰었으므로 마지막 칸이 비어있음. 유효한 타일이 아님
#         return 0
#     if idx == n:  # 완전히 채워진 경우이므로 1 반환
#         return 1
#     if memo[idx]:
#         return memo[idx]
#
#     memo[idx] = counting(idx + 2, n, memo) * 2  # 2 * 1 두 개 또는 2 * 2 한 개로 채운 경우
#     memo[idx] += counting(idx + 1, n, memo)  # 1 * 2로 채운 경우
#     memo[idx] %= 10007
#     return memo[idx]
#
#
# def solution():
#     n = int(sys.stdin.readline())
#     print(counting(0, n, [0] * n))


def solution():  # 바텀업
    n = int(sys.stdin.readline())
    if n == 1:
        print(1)
        return
    elif n == 2:
        print(3)
        return

    result = 0
    result_pprev, result_prev = 1, 3
    for i in range(2, n):
        result = (result_prev + result_pprev * 2) % 10007
        result_pprev = result_prev
        result_prev = result
    print(result)


solution()
