"""

"""
import sys


sys_input = sys.stdin.readline

n, m = map(int, sys_input().split())
cards_list = [list(map(int, sys_input().split())) for _ in range(n)]

print(max([min(cards) for cards in cards_list]))
