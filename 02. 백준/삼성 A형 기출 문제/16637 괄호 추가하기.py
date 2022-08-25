"""

"""
import sys


def get_max_value(exp_list, comb_result, idx, mid_result):
    if idx >= len(exp_list):  # 식의 계산이 모두 끝나면 결과 반환
        return mid_result
    
    if idx == 0:  # 첫 숫자의 경우 이전 연산자가 없으므로 첫 번째 값을 mid_result로 넘겨줌
        non_paren = exp_list[0]
        paren = comb_result[0]
    elif idx > 0:  #
        non_paren = mid_result
        paren = mid_result

        if exp_list[idx - 1] == '+':
            non_paren += exp_list[idx]
            paren += comb_result[idx >> 1]
        elif exp_list[idx - 1] == '*':
            non_paren *= exp_list[idx]
            paren *= comb_result[idx >> 1]
        else:
            non_paren -= exp_list[idx]
            paren -= comb_result[idx >> 1]

    return max(get_max_value(exp_list, comb_result, idx + 2, non_paren),
               get_max_value(exp_list, comb_result, idx + 4, paren))


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    exp_str = sys_input().rstrip()
    exp_list = list(map(lambda x: int(x) if x.isnumeric() else x, exp_str))
    comb_result = [eval(exp_str[i:i + 3]) for i in range(0, n, 2)]
    print(get_max_value(exp_list, comb_result, 0, 0))


solution()
