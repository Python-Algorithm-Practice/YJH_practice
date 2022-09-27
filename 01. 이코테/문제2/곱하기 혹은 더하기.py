"""

"""
import sys


def solution():
    answer = 0
    for ch in list(sys.stdin.readline().rstrip()):
        num = int(ch)
        if answer + num > answer * num:
            answer += num
        else:
            answer *= num
    print(answer)


solution()
