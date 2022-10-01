"""

"""
import sys


def solution():
    ugly_n = int(sys.stdin.readline())

    if ugly_n == 1:
        print(1)
        return

    ugly_idx = 1
    num = 1
    while ugly_idx < ugly_n:
        num += 1
        if num % 2 == 0 \
                or num % 3 == 0 \
                or num % 5 == 0:
            ugly_idx += 1
    print(num)


solution()
