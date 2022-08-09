"""

"""


n, k = map(int, input().split())

count = 0
while n > 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        diff = n // k * k
        count += n - diff
        n = diff

print(count)
