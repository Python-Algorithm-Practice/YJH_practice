"""
0의 집합을 1로 바꾸거나 1의 집합을 0으로 바꾸거나,
    둘 중 더 적은 수 선택
"""
import sys


def solution():
    string = sys.stdin.readline()

    counts = [0, 0]
    for i in range(1, len(string)):
        if string[i - 1] != string[i]:
            counts[int(string[i - 1])] += 1

    print(min(counts))


solution()
