"""
우선순위를 따르는 것이 아니라 앞에서부터 계산하기 때문에 모든 경우를 세지 않아도 된다.
앞에서부터 곱하기나 더하기 결과 중 큰값을 취하며 계산해 나가면 된다.
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
