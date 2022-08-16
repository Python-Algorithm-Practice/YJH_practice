import random


n, m = 1000, 1000

with open('testcase.txt', 'w', encoding='utf-8') as f:
    f.write(f'{n} {m}\n')
    for _ in range(n):
        line = ''.join([str(random.randint(0, 1)) for _ in range(m)])
        f.write(line + '\n')
