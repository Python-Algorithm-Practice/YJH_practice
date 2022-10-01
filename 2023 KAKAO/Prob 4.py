"""

"""


def dec_to_bin(number):
    number_str = str(bin(number))[2:]

    bin_size = 1
    while bin_size - 1 < len(number_str):
        bin_size <<= 1

    return "0" * (bin_size - 1 - len(number_str)) + number_str


def expressable(number_str, begin, end):
    if begin == end:
        return True
    mid = (begin + end) >> 1

    if number_str[mid] == '0':  # 현재 노드가 0이라면 자식들이 존재해서는 안 됨
        for idx in range(begin, end + 1):
            if number_str[idx] == '1':  # 현재 노드를 포함한 자식 계층에 유효 노드가 있다면 False 반환
                return False
        return True

    left_result = expressable(number_str, begin, mid - 1)
    right_result = expressable(number_str, mid + 1, end)

    return left_result and right_result


def solution(numbers):
    answer = []

    for number in numbers:
        number_str = dec_to_bin(number)
        answer.append(int(expressable(number_str, 0, len(number_str) - 1)))

    return answer


print(solution([63, 111, 95]))
