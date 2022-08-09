"""

"""


n = int(input())

count = 0
for i in range(n + 1):
    if '3' in str(i):  # 시간에 3이 포함되어 있으면 분, 초까지 계산하지 않아도 됨
        count += 60 * 60
        continue
    for j in range(60):  # 분에 3이 포함되어 있으면 초까지 계산하지 않아도 됨
        if '3' in str(j):
            count += 60
            continue
        for k in range(60):
            if '3' in str(k):
                count += 1

print(count)
