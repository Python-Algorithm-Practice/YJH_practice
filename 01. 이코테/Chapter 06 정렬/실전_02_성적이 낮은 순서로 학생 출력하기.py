"""

"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    students = []
    for _ in range(n):
        name, score = sys_input().split()
        students.append((int(score), name))
    students.sort()

    for i in range(n):
        print(students[i][1], end=' ')
    print()


solution()
