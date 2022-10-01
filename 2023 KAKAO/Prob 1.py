"""

"""


def date_to_day(date):
    y, m, d = map(int, date.split("."))
    return y * 28 * 12 + m * 28 + d


def solution(today, terms, privacies):
    # {Key: Value} -> {개인정보 종류: 보관일(일)}
    terms_dict = {}
    for term in terms:
        info = term.split()
        terms_dict[info[0]] = int(info[1]) * 28

    day_today = date_to_day(today)  # 오늘 일자를 일 단위로 변환
    answer = []  # 파기할 정보
    for idx, privacy in enumerate(privacies):  # 각 개인정보 약관의 파기 여부 확인
        date, doc = privacy.split()
        day_date = date_to_day(date)  # 보관 시작일자 변환
        diff = day_today - day_date  # 지난 일수 구하기
        if terms_dict[doc] <= diff:  # 보관 가능일보다 지났다면 파기할 정보에 저장
            answer.append(idx + 1)

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
