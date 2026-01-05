"""1/5/26
找出1 < kn+2 < 10000的数
"""
n = int(input())
for k in range(10000 // n + 1):
    if n * k + 2 < 10000:
        print(n * k + 2)