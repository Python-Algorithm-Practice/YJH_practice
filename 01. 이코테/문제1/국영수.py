"""
BOJ 10825 https://www.acmicpc.net/problem/10825
참조: https://codechacha.com/ko/python-sorting-dict/
"""
import sys
from functools import cmp_to_key


def cmp(a, b):
    # 국어 점수 내림차순
    if a[1] != b[1]:
        return -12 if a[1] > b[1] else 1
    # 영어 점수 오름차순
    if a[2] != b[2]:
        return -1 if a[2] < b[2] else 1
    # 수학 점수 내림차순
    if a[3] != b[3]:
        return -1 if a[3] > b[3] else 1
    # 이름 오름차순
    if a[0] != b[0]:
        return -1 if a[0] < b[0] else 1
    return 0

def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())  # 학생수
    students = []  # 학생 정보
    for _ in range(n):
        student = sys_input().rstrip().split()  # 학생 정보 입력
        students.append([student[0]] + list(map(int, student[1:])))  # 점수만 정수로 변환해 저장
    students.sort(key=cmp_to_key(cmp))  # cmp 함수 -> key 변환, key에 따라 정렬
    for student in students:  # 출력
        print(student[0])

    # compareTo() -> key()


solution()
