"""

"""
import sys


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


def simulation(perm, innings):
    score = 0  # 총점
    order = 0  # 1번 타자부터 시작

    for inning in innings:
        base_state = [False] * 4  # 타석, 1루, 2루, 3루
        out_count = 0
        score_stk = []
        while out_count < 3:
            base_state[0] = True  # 타석에 들어섬

            if inning[perm[order]] == 0:  # 아웃 -> 아웃 카운트 증가
                out_count += 1
            else:  # 1루타 이상 -> 안타 스택에 삽입
                score_stk.append(inning[perm[order]])
            order = (order + 1) % 9  # 다음 순서로 넘어감

        # 이닝이 종료되면 stack[top - 1] += stack[top] 해주며 점수 계산
        # 만약 stack의 마지막 값이 3을 넘긴다면,
        # 해당 주자를 포함하여 그 이전의 주자들 모두 홈에 들어왔다는 것이므로 스택의 길이만큼 점수 증가
        # Ex) [0:top] [1, 2, 1, 2, 1] -> 이 경우 마지막 두 주자는 이닝이 끝났을 때 3, 1루에 위치해 있음
        # 1: [1, 2, 1, 3] (+1)
        # 2: [1, 2, 4] (+3) -> 스택의 top이 3을 넘겼으므로 스택의 모든 주자는 1점씩 득점한 것
        # 왜? 내 뒷 주자보다 늦게 홈에 들어갈 수 없음. 다시 말해 내가 홈에 들어간다면 내 앞의 주자 모두 이미 홈에 들어갔다는 뜻
        while score_stk:  # 이닝이 종료됐을 때 아직 들어가지 못 한 주자들 pop()
            if score_stk[-1] > 3:  # 홈에 들어간 주자를 발견하면 그 이전 주자 모두 홈에 들어간 것이므로 점수에 스택 길이를 더함
                score += len(score_stk)
                break
            # 진루 계산
            top = score_stk.pop()
            if score_stk:
                score_stk[-1] += top
    
    return score


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    innings = [list(map(int, sys_input().split())) for _ in range(n)]

    arr = [1, 2, 3, 0, 4, 5, 6, 7, 8]  # 가능한 첫 순서

    max_score = simulation(arr, innings)
    while next_permutation(arr):
        if arr[3] == 0:  # 1번 선수가 4번 타자인 경우만 시뮬레이션
            max_score = max(max_score, simulation(arr, innings))
    print(max_score)


solution()
