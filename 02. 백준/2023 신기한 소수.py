"""
1. 2, 3, 5, 7 부터 시작
2. 아래 조건문 수행
    1) 소수가 아닌 경우 return
    2) 길이가 N 도달한 경우 출력
    3) 1, 3, 5, 7, 9 하나씩 붙이기
    4) 재귀 호출
참조: https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
"""
import sys
from math import sqrt


def is_prime(n):  # 소수 판별
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def print_prime(num, depth, max_depth):
    if not is_prime(num):  # 소수가 아닐 경우 더 할 필요없음
        return
    if depth == max_depth:  # 최종 자릿수 도달 시 출력 후 종료
        print(num)
        return

    num *= 10  # 자릿수 증가
    for i in range(1, 10, 2):  # 홀수 붙이고 재귀 호출
        print_prime(num + i, depth + 1, max_depth)


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    digit_1_primes = [2, 3, 5, 7]
    for prime in digit_1_primes:
        print_prime(prime, 1, n)


solution()
