"""

"""
import sys


# UPDATE r c value
#   (r, c) -> cell id 변환 -> cell id로 해당 cell이 속한 root cell id 구하기
#   root cell id -> (r, c) 변환
#   root_r, root_c value 삽입

# UPDATE value1 value2 : 완탐

# MERGE r1 c1 r2 c2
#   (r1, c1) cell id -> cell1, (r2, c2) cell id -> cell2 구하기
#   cell2의 root cell id를 cell1으로 설정

# UNMERGE r c
#   완탐 하면서 root cell id가 cell(r, c) 인 것들 모두 root cell id를 본인으로 변경 및 (r, c) 값 삽입

# PRINT r c
#   (r, c) root cell id 구하기
#   root cell id -> (root_r, root_c) 변환
#   return values(root_r, root_c)


def get_row_col(cell_id):
    return cell_id // 50, cell_id % 50


def get_cell_id(r, c):
    return r * 50 + c


def get_root_cell_id(root_cell, cell_id):
    if root_cell[cell_id] != cell_id:
        root_cell[cell_id] = get_root_cell_id(root_cell, root_cell[cell_id])
    return root_cell[cell_id]


def solution(commands):
    sys.setrecursionlimit(3000)
    answer = []

    values = [['' for _ in range(50)] for _ in range(50)]

    root_cell = [i for i in range(2500)]  # 50 X 50

    for command in commands:
        info = command.split()

        if info[0] == 'UPDATE':
            if len(info) == 3:  # replace
                for i in range(50):
                    for j in range(50):
                        if values[i][j] == info[1]:
                            values[i][j] = info[2]
            else:  # set new value
                cell_id = get_cell_id(int(info[1]) - 1, int(info[2]) - 1)
                root_cell_id = get_root_cell_id(root_cell, cell_id)
                root_r, root_c = get_row_col(root_cell_id)
                values[root_r][root_c] = info[3]

        elif info[0] == 'MERGE':
            r1, c1, r2, c2 = map(lambda x: int(x) - 1, info[1:])
            cell_id_1 = get_cell_id(r1, c1)  # 기준 cell id
            cell_id_2 = get_cell_id(r2, c2)  # 합쳐질 cell id
            root_cell_id_1 = get_root_cell_id(root_cell, cell_id_1)  # 기준 cell id의 root cell id
            root_cell_id_2 = get_root_cell_id(root_cell, cell_id_2)  # 합쳐질 cell id의 root cell id
            root_cell[root_cell_id_2] = root_cell_id_1  # 합쳐질 셀의 root cell id를 기존 root cell id로 설정해서 병합

            # 값 설정
            r1, c1 = get_row_col(root_cell_id_1)
            r2, c2 = get_row_col(root_cell_id_2)
            if not values[r1][c1]:
                values[r1][c1] = values[r2][c2]

        elif info[0] == 'UNMERGE':
            r, c = int(info[1]) - 1, int(info[2]) - 1
            cell_id_to_unmerge = get_cell_id(r, c)  # 병합 해제될 기준 cell id 구하기
            # 해당 셀을 모두 해제하기 위한 root cell id 구하기
            root_cell_id_to_unmerge = get_root_cell_id(root_cell, cell_id_to_unmerge)
            # 값을 보존하기 위해 root cell의 row, col을 구해서 값 보관
            root_r, root_c = get_row_col(root_cell_id_to_unmerge)
            origin_value = values[root_r][root_c]

            # 기존 root cell id가 오염되지 않게 따로 저장
            before_root_cell_ids = []
            for cell_id in range(2500):  # 모든 셀을 확인하면서,
                root_cell_id = get_root_cell_id(root_cell, cell_id)
                if root_cell_id == root_cell_id_to_unmerge:  # 만약 병합이 해제될 셀에 속해 있다면,
                    before_root_cell_ids.append(cell_id)
            for cell_id in before_root_cell_ids:
                root_cell[cell_id] = cell_id  # 해당 셀의 root cell id를 본인으로 설정해주고
                cur_r, cur_c = get_row_col(cell_id)  # 빈 값을 삽입할 위치를 구한 뒤,
                values[cur_r][cur_c] = ''  # 빈 값 삽입
            values[r][c] = origin_value

        else:  # PRINT
            r, c = int(info[1]) - 1, int(info[2]) - 1  # 출력할 cell의 행렬 좌표
            root_cell_id = get_root_cell_id(root_cell, get_cell_id(r, c))  # 출력할 셀의 root cell id
            r, c = get_row_col(root_cell_id)  # root cell id를 좌표로 변환
            answer.append(values[r][c] if values[r][c] else "EMPTY")  # root cell 값 출력

    return answer


# print(
#     solution([
#         "UPDATE 1 1 menu",
#         "UPDATE 1 2 category",
#         "UPDATE 2 1 bibimbap",
#         "UPDATE 2 2 korean",
#         "UPDATE 2 3 rice",
#         "UPDATE 3 1 ramyeon",
#         "UPDATE 3 2 korean",
#         "UPDATE 3 3 noodle",
#         "UPDATE 3 4 instant",
#         "UPDATE 4 1 pasta",
#         "UPDATE 4 2 italian",
#         "UPDATE 4 3 noodle",
#         "MERGE 1 2 1 3",
#         "MERGE 1 3 1 4",
#         "UPDATE korean hansik",
#         "UPDATE 1 3 group",
#         "UNMERGE 1 4",
#         "PRINT 1 3",
#         "PRINT 1 4"
#         ])
# )

print(
    solution([
        "PRINT 1 1",
        "PRINT 1 2",
        "PRINT 2 1",
        "PRINT 2 2",
        "MERGE 1 1 1 2",
        "MERGE 2 1 2 2",
        "MERGE 1 1 2 1",
        "UNMERGE 1 2",
        "UPDATE 2 2 VALUE",
        "PRINT 1 1",
        "PRINT 1 2",
        "PRINT 2 1",
        "PRINT 2 2",
    ])
)
