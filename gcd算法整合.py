"""1/9/26
gcd经常记不住就回来看看吧
这大概是今天比较大的收获了吧
绝不会再写一个文档来记忆最大公约数了
绝对
"""
# 欧几里得(辗转相除法)   记忆前两个吧, 暴力没什么用
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
print(gcd(a, b))

# 精简欧几里得
def gcd(a, b):
    return gcd(b, a % b) if b else a

a, b = map(int, input().split())
print(gcd(a, b))

# 内置函数
import math

a, b = map(int, input().split())
print(math.gcd(a, b))  # Python 3.5+ 内置

# 暴力枚举
def gcd(a, b):
    # 从较小的数开始递减寻找
    min_num = min(a, b)
    for i in range(min_num, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1  # 1是所有数的公约数

a, b = map(int, input().split())
print(gcd(a, b))

# 此外lcm算法为
def lcm(a, b):
    """计算最小公倍数"""
    return a * b // gcd(a, b)