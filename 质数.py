"""1/7/26
"""
def isprime(s):
    if s < 2:                    # 质数应该是大于1的自然数
        return False
    elif s == 2 or s == 3:       # 2和3是质数
        return True
    if s % 2 == 0 or s % 3 == 0: # 为2和3倍数时返回False
        return False

    i = 5                        # 在3以后, 6k+-1的数可能为质数, 从5开始步进
    while i * i <= s:            # 缩小寻找范围, 因为合数的两个质因子必有一个小于根号s
        if s % i == 0 or s % (i + 2) == 0:
             return False        # 为6k+-1倍数时返回False
        i += 6                   # 步进

    return True                  # 多轮取余后仍满足条件, 判断为质数

n = int(input())
for _ in range(n):
    s = int(input())
    if isprime(s):
        print(f"{s} is prime")
    else:
        print(f"{s} is not prime")