"""
15C8 * 8! = 2.5억
"""


def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i == 0:
        return False

    j = len(arr) - 1
    while arr[i - 1] >= arr[j]:
        j -= 1

    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return True


def set_position(n, weak, dist, pos, cur_point):
    dest = (len(weak) + cur_point - 1) % len(weak)

    for friend_count in range(len(pos)):
        next_point = cur_point
        between = 0
        while between <= dist[pos[friend_count]]:
            if next_point == dest:
                return friend_count + 1
            next_point = (next_point + 1) % len(weak)
            between = (n + weak[next_point] - weak[cur_point]) % n
        cur_point = next_point

    return int(1e9)


def solution(n, weak, dist):
    dist.sort(reverse=True)
    dist = dist[:len(weak)]

    answer = int(1e9)
    for begin_idx in range(len(weak)):
        pos = [i for i in range(len(dist))]
        while next_permutation(pos):
            abc = set_position(n, weak, dist, pos, begin_idx)
            print(abc)
            answer = min(answer, set_position(n, weak, dist, pos, begin_idx))

    return answer if answer != int(1e9) else -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
print(solution(12, [1, 3, 4], [1, 1, 1]))
