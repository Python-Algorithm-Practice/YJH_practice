"""
BOJ 15483 https://www.acmicpc.net/problem/15483
"""
import sys


def counting(a, a_idx, b, b_idx, memo):
    if a_idx == len(a):
        return len(b) - b_idx
    elif b_idx == len(b):
        return len(a) - a_idx

    # a_idx, b_idx일 때 구했던 결과가 있다면 해당 결과 반환
    if memo[a_idx][b_idx]:
        return memo[a_idx][b_idx]

    # 현재 각 문자가 같으면 삽입, 삭제, 교체를 할 필요없이 바로 다음 문자로 판별
    if a[a_idx] == b[b_idx]:
        memo[a_idx][b_idx] = counting(a, a_idx + 1, b, b_idx + 1, memo)
        return memo[a_idx][b_idx]

    # 삽입, 문자열 A의 a_idx에 b[b_idx]를 삽입했다고 가정하고 다음 함수 호출
    min_count = counting(a, a_idx, b, b_idx + 1, memo)

    # 삭제, A[a_idx]를 지웠다고 가정하고 다음 함수 호출
    min_count = min(min_count, counting(a, a_idx + 1, b, b_idx, memo))

    # 교체, A[a_idx]를 B[b_idx]로 교체했다고 가정하고 다음 함수 호출
    min_count = min(min_count, counting(a, a_idx + 1, b, b_idx + 1, memo))

    # a_idx, b_idx일 때 결과가 또 필요할 수 있으므로 따로 저장
    memo[a_idx][b_idx] = min_count + 1
    return memo[a_idx][b_idx]


def solution():
    sys_input = sys.stdin.readline

    a = sys_input().rstrip()
    b = sys_input().rstrip()

    print(counting(a, 0, b, 0, [[0] * (len(b) + 1) for _ in range(len(a) + 1)]))


sys.setrecursionlimit(1000000)  # 1000 * 1000이므로 최대 100만?
solution()
