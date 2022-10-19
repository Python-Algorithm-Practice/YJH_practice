"""
완탐, O(M * N^2)
"""
import sys


def make_steps(n):
    """
    이동 좌표 미리 구해두기 (e.g. [(1, 0), (2, 0), (2, 1), (2, 2), ..., (0, 0)] )
    길이: N^2 - 1 (시작점 제외)
    
    알고리즘:
        (0, 0)부터 시작해서 오른쪽으로 쭉 이동,
        아래로 쭉 이동,
        왼쪽으로 쭉 이동,
        위로 쭉 이동,
        계속 반복하면서 좌표를 저장하고 모두 저장한 뒤에는 reversed로 배열 뒤집기
    """
    r = c = 0
    steps, max_steps = [], n * n  # 결과 리스트, 최대 길이

    direc = 0
    local_dr, local_dc = [0, 1, 0, -1], [1, 0, -1, 0]
    visit = [[False] * n for _ in range(n)]

    while len(steps) < max_steps:
        steps.append((r, c))
        visit[r][c] = True
        r, c = r + local_dr[direc], c + local_dc[direc]
        if r < 0 or n <= r or c < 0 or n <= c or visit[r][c]:  # 다음 지점이 범위 밖이거나 이미 방문한 점이라면,
            r, c = r - local_dr[direc], c - local_dc[direc]  # 이전으로 돌아가서,
            direc = (direc + 1) % 4  # 방향을 바꾸고,
            r, c = r + local_dr[direc], c + local_dc[direc]  # 다음 지점 찾기

    steps.pop()
    return list(reversed(steps))


def blizzard(board, d, s, dr, dc):
    score = 0
    r = c = len(board) >> 1  # 중심점
    for _ in range(s):
        r, c = r + dr[d], c + dc[d]  # 블리자드 다음 지점
        score += board[r][c]  # ! 점 수 획 득 !
        board[r][c] = 0  # ! 구 슬 파 괴 !
    return score


def pull(board, steps):
    """
    공백 좌표와 구슬 좌표를 찾고, 값을 교환하면서 원소 당기기
    """
    space_idx = bead_idx = 0

    # 공백 좌표와 구슬 좌표를 조정하여 초기 설정하기
    while bead_idx < len(steps) \
            and board[steps[bead_idx][0]][steps[bead_idx][1]] != 0:
        space_idx += 1
        bead_idx += 1

    # 당기기 시작
    while bead_idx < len(steps):
        # 당길 구슬 찾기
        while bead_idx < len(steps) \
                and board[steps[bead_idx][0]][steps[bead_idx][1]] == 0:
            bead_idx += 1
        # 교환하여 구슬 당기고, 공백 좌표와 구슬 좌표 1 씩 증가
        while bead_idx < len(steps) \
                and board[steps[bead_idx][0]][steps[bead_idx][1]] != 0:
            # 교환 및 다음 원소로 넘어가기
            board[steps[bead_idx][0]][steps[bead_idx][1]], board[steps[space_idx][0]][steps[space_idx][1]] \
                = board[steps[space_idx][0]][steps[space_idx][1]], board[steps[bead_idx][0]][steps[bead_idx][1]]
            space_idx += 1
            bead_idx += 1


def bomb(board, steps):
    score = cont_count = prev_value = idx = 0
    # 모두 순회하거나 빈 공간을 만날 때까지 반복, 구슬은 모두 당겨진 상태이므로 빈 공간을 만났다는 건 모든 구슬을 확인했다는 뜻
    while idx < len(steps) and board[steps[idx][0]][steps[idx][1]] != 0:
        # 현재 지점과 값 확인
        r, c = steps[idx]
        cur_value = board[r][c]
        if prev_value != cur_value:  # 이전 값과 다르다면 현재까지 계산한 연속횟수를 반영해주어야 함
            if cont_count >= 4:  # 구슬의 개수까지 4 이상이라면, 점수 계산하고 연속하는 횟수만큼 ! 구 슬 파 괴 !
                score += cont_count * prev_value
                for bomb_idx in range(idx - cont_count, idx):
                    board[steps[bomb_idx][0]][steps[bomb_idx][1]] = 0
            cont_count = 0  # 연속횟수 계산 완료했으므로 초기화
        cont_count += 1  # 이전 값과 같든 다르든 연속횟수 1 증가
        prev_value = cur_value  # 다음으로 넘어가야 하므로 이전 값 갱신
        idx += 1
    # 모두 끝마치고 연속횟수 세기
    if cont_count >= 4:
        score += cont_count * prev_value
        for bomb_idx in range(idx - cont_count, idx):
            board[steps[bomb_idx][0]][steps[bomb_idx][1]] = 0
    return score


def change(board, steps):
    """
    bomb() 함수와 알고리즘은 똑같음
    다만 다른 값을 만났을 때 해당 구슬을 터뜨리는 게 아니라 new_values에 [연속횟수, 구슬 번호]를 추가해줌
    """
    new_values = []
    cont_count = prev_value = idx = 0
    while idx < len(steps) and board[steps[idx][0]][steps[idx][1]] != 0:
        r, c = steps[idx]
        cur_value = board[r][c]
        if prev_value != cur_value and prev_value != 0:
            new_values += [cont_count, prev_value]
            cont_count = 0
        cont_count += 1
        prev_value = cur_value
        idx += 1
    if cont_count:
        new_values += [cont_count, prev_value]
    idx = 0
    while idx < len(steps):
        board[steps[idx][0]][steps[idx][1]] = new_values[idx] if idx < len(new_values) else 0
        idx += 1


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    dr = [0, -1, 1, 0, 0]  # _, 상, 하, 좌, 우
    dc = [0, 0, 0, -1, 1]

    # 이동 좌표, 움직일 방향 목록
    steps = make_steps(n)

    score = 0
    for _ in range(m):
        d, s = map(int, sys_input().split())
        blizzard(board, d, s, dr, dc)  # !!! 블리자드 !!!
        pull(board, steps)  # 구슬 앞으로 당기기

        # 연속 구슬 폭발
        bomb_score = bomb(board, steps)
        while bomb_score:
            score += bomb_score
            pull(board, steps)
            bomb_score = bomb(board, steps)

        change(board, steps)  # 구슬 변화

    print(score)


solution()

# 64
# 0 1
# 2 2 3 3
# 0 0 0 1 1 1
# 2 2 2 2 3 3 3 3
# 0 0 0 0 0 1 1 1 1 1
# 2 2 2 2 2 2 3 3 3 3 3 3
# 0 0 0 0 0
