"""
스택, O(N)

String: 12ab112ab2ab
Explosion: 12ab

0. 스택 생성 및 더미 데이터 삽입
    Stack = [(?, 0)]

1. 문자, 인덱스: '1', 0
    Stack = [(?, 0), ('1', 1)]      => Explosion[stack.top]과 같으므로 1 더해서 스택에 삽입

2. 문자, 인덱스: '2', 1
    Stack = [(?, 0), ('1', 1), ('2', 2)]        => 1번과 같음

3. 문자, 인덱스: 'a', 2
    Stack = [(?, 0), ('1', 1), ('2', 2), ('a', 3)]          => 1번과 같음

4. 문자, 인덱스: 'b', 3
    Stack = [(?, 0), ('1', 1), ('2', 2), ('a', 3), ('b', 4)]            => 1번과 같음
    ->
    Stack = [(?, 0)]        => stack.top이 Explosion 길이와 같아졌으므로 해당 길이만큼 pop()

5. 문자, 인덱스: '1', 4
    Stack = [(?, 0), ('1', 1)]      => 1번과 같음

6. 문자, 인덱스: '1', 5
    Stack = [(?, 0), ('1', 1), ('1', 1)]        => String[5] != Explosion[stack.top]이지만, Explosion[0]과는 같다.
                                                    바꿔 말하면 String[5]에서 폭발 문자열이 다시 시작될 수 있으므로 처음부터 시작

7. 문자, 인덱스: '2', 6
    Stack = [(?, 0), ('1', 1), ('1', 1), ('2', 2)]          => 1번과 같음
8. 문자, 인덱스: 'a', 7
    Stack = [(?, 0), ('1', 1), ('1', 1), ('2', 2), ('a', 3)]        => 1번과 같음
9. 문자, 인덱스: 'b', 8
    Stack = [(?, 0), ('1', 1), ('1', 1), ('2', 2), ('a', 3), ('b', 4)]          => 1번과 같음
    ->
    Stack = [(?, 0), ('1', 1)]      => 4번과 같음

10. 이하 7 ~ 9번과 같음

11. 최종 스택 Stack = [(?, 0)] => "FRULA"
"""
import sys


def solution():
    sys_input = sys.stdin.readline

    string = sys_input().rstrip()
    explosion = sys_input().rstrip()

    stack = [('', 0)]  # 스택 구조 [(ch, exp_idx), ...], 더미 데이터로 초기화, exp_idx = 현재 문자가 몇 번째 폭발 문자과 일치하는지
    for ch in string:
        if ch == explosion[stack[-1][1]]:  # 폭발 문자와 같다면 일치 횟수 증가
            stack.append((ch, stack[-1][1] + 1))
        elif ch == explosion[0]:  # 다른데 첫 번째 폭발 문자와 같다면 일치 횟수 1부터 시작
            stack.append((ch, 1))
        else:  # 그냥 아예 다르다면 0부터 시작
            stack.append((ch, 0))
        if stack[-1][1] == len(explosion):  # 폭발 문자열을 완성했다면 해당 길이만큼 pop()
            for _ in range(len(explosion)):
                stack.pop()

    answer = ''
    for i in range(1, len(stack)):
        answer += stack[i][0]
    print(answer if answer else 'FRULA')


solution()
