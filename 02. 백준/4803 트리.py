"""

"""
import sys


def find_parent(root, idx):
    if idx == root[idx]:  # 루트 노드일 경우 해당 인덱스 반환
        return idx
    root[idx] = find_parent(root, root[idx])  # 추후 루트 노드 탐색 시 빠르게 접근하기 위해, 얻은 루트 정보로 갱신
    return root[idx]


def solution():
    sys_input = sys.stdin.readline

    case = 0

    n, m = map(int, sys_input().split())
    while n or m:
        edges = [list(map(int, sys_input().split())) for _ in range(m)]  # 간선 입력

        tree_count = n
        root = [i for i in range(n + 1)]  # 각 정점의 root 노드의 번호 저장
        rank = [1] * (n + 1)  # 각 정점이 속한 트리의 노드 개수 (사실상 root 노드의 정보만 유효)

        for a, b in edges:
            parent_a = find_parent(root, a)  # 노드 a의 루트
            parent_b = find_parent(root, b)  # 노드 b의 루트

            if parent_a != parent_b:  # 노드 a의 루트와 b의 루트가 다르면 두 트리를 병합
                tree_count -= 1  # 두 개의 트리가 하나로 합쳐지므로 전체 트리의 개수 1 감소
                if rank[a] < rank[b]:  # 시간복잡도 개선을 위해 작은 트리를 큰 트리에 병합
                    root[parent_a] = parent_b  # 루트 번호 갱신
                    rank[parent_b] += rank[parent_a]  # 서브 노드의 개수 갱신
                else:
                    root[parent_b] = parent_a
                    rank[parent_a] += rank[parent_b]

        # (Key, Value) -> (트리의 번호, 해당 트리의 간선 개수) 정보를 저장하는 딕셔너리 생성
        edge_count = dict()
        for node, _ in edges:  # 두 노드 모두 같은 트리에 속하므로 하나의 노드 정보만 알면 됨
            tree_num = find_parent(root, node)  # 트리 번호 확인
            # 해당 트리의 간선 개수 갱신
            if tree_num in edge_count:
                edge_count[tree_num] += 1
            else:
                edge_count[tree_num] = 1

        # 각 트리를 순회하는데, 그래프로 판별 시 전체 트리의 개수를 1 감소
        # 그래프 판별은 (트리에 속한 정점의 개수 - 1) == 간선의 개수로 판별
        for tree_num in edge_count:
            if rank[tree_num] - 1 != edge_count[tree_num]:
                tree_count -= 1

        # 트리의 개수에 따라 결과 출력
        case += 1
        if tree_count > 1:
            print('Case {}: A forest of {} trees.'.format(case, tree_count))
        elif tree_count == 1:
            print('Case {}: There is one tree.'.format(case))
        else:
            print('Case {}: No trees.'.format(case))

        n, m = map(int, sys_input().split())


solution()
