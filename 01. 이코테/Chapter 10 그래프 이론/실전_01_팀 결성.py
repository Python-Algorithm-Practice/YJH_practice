"""
BOJ 1717 집합의 표현
"""
import sys


def find_parent(set_num, n):
    if set_num[n] != n:
        set_num[n] = find_parent(set_num, set_num[n])
    return set_num[n]


def solution():
    sys_input = sys.stdin.readline
    sys_print = sys.stdout.write

    n, m = map(int, sys_input().split())

    set_num = [i for i in range(n + 1)]
    for _ in range(m):
        order, a, b = map(int, sys_input().split())
        if order == 0:
            parent_a = find_parent(set_num, a)
            parent_b = find_parent(set_num, b)
            if parent_a != parent_b:
                set_num[min(parent_a, parent_b)] = max(parent_a, parent_b)
        else:
            sys_print('YES\n' if find_parent(set_num, a) == find_parent(set_num, b) else 'NO\n')


solution()
