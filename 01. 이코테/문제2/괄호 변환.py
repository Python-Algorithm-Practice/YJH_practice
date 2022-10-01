"""

"""


def is_correct(string):
    stk = 0
    for ch in string:
        if ch == '(':
            stk += 1
        else:
            stk -= 1
        if stk < 0:
            return False
    if stk:
        return False
    return True


def divide(string):
    sep_idx = 1
    stk = 1 if string[0] == '(' else -1
    while sep_idx < len(string) and stk != 0:
        stk += 1 if string[sep_idx] == '(' else -1
        sep_idx += 1

    return string[:sep_idx], string[sep_idx:]


def turn_over(string):
    flipped = ''
    for i in range(1, len(string) - 1):
        flipped += ')' if string[i] == '(' else '('
    return flipped


def solution(p):
    if not p:
        return ''

    u, v = divide(p)
    if is_correct(u):
        return u + solution(v)

    return '(' + solution(v) + ')' + turn_over(u)


print(solution("(()())()"))
