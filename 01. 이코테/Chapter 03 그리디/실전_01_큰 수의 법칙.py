"""

"""
import sys


sys_input = sys.stdin.readline

n, m, k = map(int, sys_input().split())
nums = list(map(int, sys_input().split()))
nums.sort()

max1 = nums[-1]
max2 = nums[-2]

cycle_value = max1 * k + max2

answer = 0
if m > k:
    answer = m // (k + 1) * cycle_value
    m %= k + 1
answer += m * max1

print(answer)
