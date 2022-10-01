"""

"""
import sys


def dfs(n, m, x, y, r, c, k):
    if k == 0 and x == r and y == c:
        return '_'  # 목표를 찾았음을 알리는 의미로 _ 반환
    dist = abs(r - x) + abs(c - y)
    if k < dist:
        return None
    k -= 1

    if x + 1 < n:
        result = dfs(n, m, x + 1, y, r, c, k)
        if result:
            return "d" + result
    if y > 0:
        result = dfs(n, m, x, y - 1, r, c, k)
        if result:
            return "l" + result
    if y + 1 < m:
        result = dfs(n, m, x, y + 1, r, c, k)
        if result:
            return "r" + result
    if x > 0:
        result = dfs(n, m, x - 1, y, r, c, k)
        if result:
            return "u" + result
    return None


def solution(n, m, x, y, r, c, k):
    sys.setrecursionlimit(3000)
    if (abs(r - x) + abs(c - y)) & 1 != k & 1:
        return "impossible"
    answer = dfs(n, m, x - 1, y - 1, r - 1, c - 1, k)
    answer = answer.replace('_', '') if answer else 'impossible'
    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))
