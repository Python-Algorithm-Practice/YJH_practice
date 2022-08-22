"""
BOJ 1463 1로 만들기
"""
import sys


def solution():  # 현재 수에 대한 값을 활용해 다음 정수의 최솟값 갱신
    n = int(sys.stdin.readline())
    memo = [1000000 for _ in range(n + 1)]
    memo[1] = 0

    for i in range(1, n + 1):
        if i + 1 <= n:
            memo[i + 1] = min(memo[i + 1], memo[i] + 1)

        mul_2 = i * 2
        if mul_2 <= n:
            memo[mul_2] = min(memo[mul_2], memo[i] + 1)

        mul_3 = i * 3
        if mul_3 <= n:
            memo[mul_3] = min(memo[mul_3], memo[i] + 1)

    print(memo[n])


# def solution():  # 이전에 나왔던 수를 활용해 현재 정수의 최솟값 갱신
#     n = int(sys.stdin.readline())
#     memo = [1000000 for _ in range(n + 1)]
#     memo[1] = 0
#
#     for i in range(2, n + 1):
#         memo[i] = min(memo[i], memo[i - 1] + 1)
#
#         if i % 2 == 0:
#             memo[i] = min(memo[i], memo[i >> 1] + 1)
#
#         if i % 3 == 0:
#             memo[i] = min(memo[i], memo[i // 3] + 1)
#
#     print(memo[n])


solution()
