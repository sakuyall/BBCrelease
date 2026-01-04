"""1/4/26
"""
# 简单写法
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# 优化写法
"""
一个数的约数是成对存在的, 一个小一个大, 分布在根号n的两侧
因此只需寻找一侧, 另一侧的结果是重复的
n%i==0时i是约数, 此时另一个约数就是n//i
同时需要排除n为完全平方数情况, 此时n只有一个约数, 添加一次即可
"""
n = int(input())
divisors = []  # 存储所有约数的列表

i = 1
while i * i <= n:  # 相当于 i <= sqrt(n)，但不用算平方根
    if n % i == 0:  # 如果i是约数
        divisors.append(i)          # 添加小约数
        if i != n // i:             # 如果不是完全平方数的情况
            divisors.append(n // i)  # 添加大约数
    i += 1

divisors.sort()  # 排序，因为我们是成对添加的，顺序是乱的
for d in divisors:
    print(d)