"""

"""
import sys


sys_input = sys.stdin.readline

n = int(sys_input())  # n 입력
coins = list(map(int, sys_input().split()))  # 화폐 단위 입력
coins.sort(reverse=True)  # 내림차순 정렬

count = 0
for coin in coins:
    count += n // coin
    n %= coin

print(count)
