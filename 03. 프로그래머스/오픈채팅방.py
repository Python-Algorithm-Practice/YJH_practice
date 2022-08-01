"""

"""


def solution(record):
    answer = []

    # (Key, Value) -> (UID, 닉네임) 정보를 저장하는 딕셔너리 생성
    nickname = dict()
    for string in record:
        info = string.split()  # 명령, UID, (닉네임)
        order, uid = info[0], info[1]  # 명령의 종류 및 UID 획득
        if order != 'Leave':
            nickname[uid] = info[2]  # 닉네임이 주어질 경우 바뀐 닉네임일 수도 있으므로 nickname 딕셔너리 갱신

    for string in record:
        info = string.split()
        order, uid = info[0], info[1]

        # 명령의 종류에 따라 최종 닉네임을 담은 문자열 저장
        if order == 'Enter':
            answer.append('%s님이 들어왔습니다.' % nickname[uid])
        elif order == 'Leave':
            answer.append('%s님이 나갔습니다.' % nickname[uid])

    return answer


print(solution(
    ["Enter uid1234 Muzi",
     "Enter uid4567 Prodo",
     "Leave uid1234",
     "Enter uid1234 Prodo",
     "Change uid4567 Ryan"]
))
