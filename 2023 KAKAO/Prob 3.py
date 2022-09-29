"""

"""


def calc(users, emoticons, dc_rates):
    result = [0, 0]

    for user in users:
        money = 0
        for price, dc_rate in zip(emoticons, dc_rates):
            if user[0] <= dc_rate:  # 기준 이상 할인하면 구매
                money += int(price * (100 - dc_rate) / 100)
        # 기준치를 넘으면 이모티콘 플러스 가입
        if user[1] <= money:
            result[0] += 1
        else:
            result[1] += money

    return result


def bruteforce(users, emoticons, dc_rates, max_result):
    if len(dc_rates) == len(emoticons):
        result = calc(users, emoticons, dc_rates)
        if max_result < result:
            max_result[0], max_result[1] = result
        return

    for dc_rate in [10, 20, 30, 40]:
        dc_rates.append(dc_rate)
        bruteforce(users, emoticons, dc_rates, max_result)
        dc_rates.pop()


def solution(users, emoticons):
    answer = [0, 0]
    bruteforce(users, emoticons, [], answer)
    return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
