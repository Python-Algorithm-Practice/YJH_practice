"""
DP, O(N * M)

왜?
    알고리즘을 알아야 납득이 되는데 알고리즘은 아래와 같다.
    N을 M개로 표현하는 방법
        ex) 20을 2개로 표현하는 방법
        1. 0 + (20을 1개로 표현하는 방법의 수)
        2. 1 + (19를 1개로 표현하는 방법의 수)
        3. 2 + (18을 1개로 표현하는 방법의 수)
        ...
        21. 20 + (0을 1개로 표현하는 방법의 수)
    인데, 200 200일 경우 이미 셌던 걸 계속 세기 때문에 방법의 수가 엄청 뿜ㅁ뿜
    (문제에서 결과를 10억으로 나누라는 말만 봐도 알 수 있음)
"""
import sys


def rCounting(n, k, memo):
    if memo[n][k] != -1:  # -1이 아닐 경우 기존에 셌던 경우이므로 해당 결과 반환
        return memo[n][k]

    # i + (n - i를 k - 1개로 표현하는 방법의 수)를 모두 구해서 메모에 더해줌
    memo[n][k] = 0
    for i in range(n + 1):
        memo[n][k] = (memo[n][k] + rCounting(n - i, k - 1, memo)) % 1000000000
    return memo[n][k]


def solution():
    n, k = map(int, sys.stdin.readline().split())
    memo = [[-1] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        memo[i][1] = 1  # N을 1개로 표현하는 방법의 수는 1개
        memo[i][0] = 0  # N을 0개로 표현하는 방법의 수는 0개
    for i in range(1, k + 1):
        memo[0][i] = 1  # 0을 K개로 표현하는 방법의 수는 1개

    print(rCounting(n, k, memo))


solution()
