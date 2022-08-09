"""

"""


loc = input()

# 현재 좌표 구하기
r = ord(loc[0]) - ord('a')
c = int(loc[1]) - 1

# 8방향으로의 이동량 구하기
move_count = [[-1, 2], [-1, -2], [1, 2], [1, -2], [-2, -1], [-2, 1], [2, -1], [2, 1]]

# 각 방향의 유효 여부 검사
count = 0
for x, y in move_count:
    if 0 <= r + x < 8 and 0 <= c + y < 8:
        count += 1

print(count)
