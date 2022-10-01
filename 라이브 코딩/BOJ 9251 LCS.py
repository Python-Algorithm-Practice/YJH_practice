"""
DP 기준
memo[i][j] = ?
    string1[:i], string2[:j] 간의 LCS 길이

    string1[i] == string2[j], 두 문자가 일치한다면?
        - string1[i - 1], string2[j - 1] 간의 LCS 길이보다 1 긺
        ex)
            ABCD, ACD 일 경우
            D, D가 같으므로, ABCD, ACD 간의 LCS 길이는 (ABC, AC)의 LCS 길이에서 1을 더한 것과 같음

    string1[i] != string2[j], 두 문자가 일치하지 않는다면?
        - (string1[i - 1], string2[j]) 또는 (string1[i], string2[j - 1]) 중 최댓값과 똑같음
        ex)
            ABCD, ACE 일 경우
            D, E가 다르므로, ABCD, ACE 간의 LCS 길이는 (ABC, ACE) 또는 (ABCD, AC) 중 최대 LCS 길이임
"""
import sys


def solution():
    sys_input = sys.stdin.readline

    string1 = sys_input().rstrip()
    string2 = sys_input().rstrip()

    memo = [[0] * len(string1) for _ in range(len(string2))]

    for i in range(len(string1)):
        if string1[i] == string2[0]:
            while i < len(string1):
                memo[0][i] = 1
                i += 1
            break
    for i in range(len(string2)):
        if string2[i] == string1[0]:
            while i < len(string2):
                memo[i][0] = 1
                i += 1
            break

    for i in range(1, len(string2)):
        for j in range(1, len(string1)):
            if string2[i] == string1[j]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

    print(memo[-1][-1])


solution()

#   A C A Y K P
# C 0 1 1 1 1 1
# A 1 1 2 2 2 2
# P 1 1 2 2 2 2
# C 1 2 2 2 2 2
# A 1 2 3 3 3 3
# K 1 2 3 3 4 4
