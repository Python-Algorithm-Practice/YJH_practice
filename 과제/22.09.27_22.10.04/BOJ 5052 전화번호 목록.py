"""
트라이 구조, O(N * Len(N)), 전화번호의 수 * 전화번호 최대 길이

왜?
    이 문제의 핵심은 어떤 전화번호가 다른 전화번호의 접두 문자열이 되는지 확인하는 것인데,
    접두 문자열이 된다면 일관성이 없는 것, 되지 않는다면 일관성이 있는 것이다.
    그런데 전화번호의 개수는 최대 1만 개이므로, 모든 문자열에 대해 비교하면 1억을 훨씬 넘을 듯요

    따라서 트라이 구조를 사용
    트라이 구조를 사용해 모든 문자열을 등록한 뒤, 리프 노드의 개수를 센다.
    만약 전화번호의 개수와 리프 노드의 개수가 같다면 기존 전화번호에 이어서 다른 전화번호가 추가된 것이 아니므로,
    일관성이 있다는 것이고, 다르다면 기존 전화번호에 이어서 다른 전화번호가 추가된 것이므로 일관성이 없다는 것이다.

    ex) 911, 97625999, 91125426
    root -> 9 -> 1 -> 1 -> (911 끝남) -> 2 -> 5 -> 4 -> 2 -> 6 (91125426 끝남)
              -> 7 -> 6 -> 2 -> 5 -> 9 -> 9 -> 9 (97625999 끝남)
    => 911에 이어 91125426이 추가되었고, 그에 따라 리프 노드는 2개이므로 일관성 Nope.

    ex) 113, 12340, 123440, 12345, 98346
    root -> 1 -> 1 -> 3 (113 끝)
              -> 2 -> 3 -> 4 -> 0 (12340 끝)
                             -> 4 -> 0 (123440 끝)
                             -> 5 (12345 끝)
         -> 9 -> 8 -> 3 -> 4 -> 6 (98346 끝)
    => 모든 전화번호가 리프 노드를 가지므로 일관성 Yup.
"""
import sys


class Trie:
    def __init__(self, num=''):
        self.num = num
        self.children = dict()


def get_leaf_count(node):  # 리프 노드 개수 세기~
    if len(node.children) == 0:
        return 1
    count = 0
    for child in node.children:
        count += get_leaf_count(node.children[child])
    return count


def solution():
    sys_input = sys.stdin.readline

    T = int(sys_input())
    for _ in range(T):
        root = Trie()  # 트라이 루트 생성
        n = int(sys_input())  # 전화번호 개수 입력
        for _ in range(n):
            cursor = root  # 전화번호를 저장하기 위한 커서를 만들어 루트로 설정
            for ch in sys_input().rstrip():  # 전화번호의 각 문자를 따라가는데,
                if ch not in cursor.children:  # 현재 커서가 가리키는 위치에 현재 문자가 없다면 노드 추가
                    cursor.children[ch] = Trie(ch)
                cursor = cursor.children[ch]  # 현재 문자의 노드로 커서 변경
        print('YES' if n == get_leaf_count(root) else 'NO')  # 리프 노드의 개수에 따라 결과 출력


solution()
