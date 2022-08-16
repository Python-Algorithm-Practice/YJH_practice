import random


n = 10000

nums = [i for i in range(1, n + 1)]
random.shuffle(nums)

with open('testcase.txt', 'w', encoding='utf-8') as f:
    f.write(str(n) + '\n')
    f.write(' '.join(map(str, nums)) + '\n')
