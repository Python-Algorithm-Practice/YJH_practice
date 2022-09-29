"""

"""


class Node:
    def __init__(self, num):
        self.num = num
        self.road_idx = 0
        self.edges = []


def express(num, count, result):
    """
    num을 count 개로 나타낼 수 있는 수의 집합을 내림차순으로 result에 담기
    ex) (5, 3, []) -> 최종 result = [3, 1, 1]
    ex) (7, 4, []) -> 최종 result = [3, 2, 1, 1]
    """
    if num < 0:
        return False
    if count == 0:
        if num != 0:
            return False
        return True

    for i in range(1, 4):
        if express(num - i, count - 1, result):
            result.append(i)
            return True
    return False


def get_leaf_node(nodes, num):
    """
    num 노드에서 시작해서 길을 따라 리프 노드까지~
    길을 지난 후에는 (리프 노드를 찾은 뒤엔) 다음 번호의 길 활성화
    """
    if not nodes[num].edges:
        return num
    leaf_node = get_leaf_node(nodes, nodes[num].edges[nodes[num].road_idx])
    nodes[num].road_idx = (nodes[num].road_idx + 1) % len(nodes[num].edges)
    return leaf_node


def solution(edges, target):
    nodes = [Node(i) for i in range(len(edges) + 1)]

    for a, b in edges:
        nodes[a - 1].edges.append(b - 1)
    for node in nodes:  # road_idx를 1씩 증가시키면서 사용하기 위해 오름차순 정렬
        node.edges.sort()

    appear_count = [0] * len(target)
    #  1: 현재까지 등장한 리프 노드 개수로 target을 나타낼 수 있음
    #  0: 아직 나타낼 수 없음
    # -1: 앞으로도 평생 나타낼 수 없음 (예를 들어, target = 1, 리프 노드 등장 횟수 = 2 일 경우, 뭔 짓을 해도 두 개의 양의 정수로 1을 나타낼 수 없음)
    expressable_state = 0
    while expressable_state == 0:  # 각 리프 노드의 등장 횟수가 자신의 target보다 많아지면 1, 2, 3으로 나타낼 수 없음
        leaf_node = get_leaf_node(nodes, 0)
        appear_count[leaf_node] += 1

        expressable_state = 1
        for i in range(len(target)):
            if target[i] < appear_count[i]:
                expressable_state = -1
                break
            elif target[i] / 3 > appear_count[i]:
                expressable_state = 0
                break

    # 표현 불가능할 경우 [-1] 반환
    if expressable_state == -1:
        return [-1]

    # 각 리프 노드마다 들어가야 하는 숫자들 (1, 2, 3 중) 계산
    express_nums = [[] for _ in range(len(nodes))]
    for i in range(len(nodes)):
        if appear_count[i]:
            express(target[i], appear_count[i], express_nums[i])

    # 길 상태 초기화
    for node in nodes:
        node.road_idx = 0

    # 계산했던 리프 노드마다 들어가야 할 숫자들 차례로 집어 넣기
    answer = []
    for _ in range(sum(appear_count)):
        answer.append(express_nums[get_leaf_node(nodes, 0)].pop())

    return answer


print(solution([[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]], [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]))
print(solution([[1, 2], [1, 3]], [0, 7, 3]))
print(solution([[1, 3], [1, 2]], [0, 7, 1]))
