"""
BOJ 2294 동전 2
"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n, k = map(int, sys_input().split())
    coins = list({int(sys_input()) for _ in range(n)})
    memo = [10000] * (k + 1)

    memo[0] = 0
    for coin in coins:
        if coin <= k:
            memo[coin] = 1

    for i in range(k):
        for coin in coins:
            if i + coin <= k:
                memo[i + coin] = min(memo[i + coin], memo[i] + 1)

    if memo[k] == 10000:
        memo[k] = -1
    print(memo[k])


solution()
