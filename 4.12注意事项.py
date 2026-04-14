一道题应限制在20分钟内做完, 十分钟没思路立刻看答案找模板
时间复杂度一般在1e7-8左右
因此若题目范围在1e5, 则可以采用on或onlogn的算法
每日两简单两中等, 无需提交github
24日开始模拟

快读模板
import sys
input = lambda:sys.stdin.readline().strip()
通过使用input(变量)获取刚才的读取内容
sys.stdin获取的是一个文件对象, 可以使用for循环进行迭代

# 十进制拆位------------------------------------
def count_2(x):
    cnt = 0
    while x > 0:
        if x % 10 == 条件:
            cnt += 1
        x //= 10
        
    return cnt

# 进制转换---------------------------------
n进制转十进制(D) 拆位 分别乘n的01234...次加一起
反转 对n做短除法, 不断取余直至商为0, 将余数倒序排

# 阶乘-------------------------------------
import math
math.factorial()

# 组合数-----------------------------------
def c(n, m):
    return math.factorial(n) // (math.factorial(m)\
                                * math.factorial(n-m))
# 错误排序----------------------------------
def d(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return (n - 1) * (d(n - 1) + d(n - 2))

# 最大公约数--------------------------------------
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# 质数-----------------------------------------
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
        
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
            
    return True

# Era----------------------------------------
n = 10 ** 7
prime = []
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, n + 1):
    if is_prime[i]:
        prime.append(i)
        if i * i > n:
            continue
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

print(prime[100001])

# 最长子序列----------------------------------

# 快速幂------------------------------------
def quick_pow(a, n, mod):
    ans = 1
    while n > 0:
        if n & 1:
            ans = ans * a % mod
        a = a * a % mod
        n >>= 1

    return ans

# DFS------------------------------------
# 排列问题
def dfs(n, cnt, li):
    if cnt == n:
        print(*li[1:])
        return

    for i in range(1, n + 1):
        if i not in li:
            li[cnt + 1] = i
            dfs(n, cnt + 1, li)
            li[cnt + 1] = 0

cnt = 0
n = int(input())
li = [0] * (n + 1)
dfs(n, cnt, li)

# BFS---------------------------------------

# 一维前缀和---------------------------------
data = sys.stdin.read().strip().split()

idx = 0
n = int(data[idx]); idx += 1
m = int(data[idx]); idx += 1

a = [0] * (n + 1)
pre = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = int(data[idx]); idx += 1
    pre[i] = pre[i - 1] + a[i]

for j in range(m):
    l = int(data[idx]); idx += 1
    r = int(data[idx]); idx += 1
    ans = pre[r] - pre[l - 1]
    print(ans)

# 二维前缀和---------------------------------
import sys
import os
from io import StringIO

data = "\
3 4 3\n\
1 7 2 4\n\
3 6 2 8\n\
2 1 2 3\n\
1 1 2 2\n\
2 1 3 4\n\
1 3 3 4"
sys.stdin = StringIO(data)

n, m, q = map(int, input().split())

a = [[0] * (m + 1) for _ in range(n + 1)]
sums = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    a[i] = [0] + list(map(int, input().split()))
    for j in range(1, m + 1):
        sums[i][j] = sums[i][j - 1] + a[i][j]
    for j in range(1, m + 1):
        sums[i][j] += sums[i - 1][j]

for k in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    ans = sums[x2][y2] + sums[x1 - 1][y1 - 1]\
          - sums[x1 - 1][y2] - sums[x2][y1 - 1]
    print(ans)

# Bisect二分---------------------------------
import bisect
arr = [1, 3, 5, 5, 7, 9]
print(bisect.bisect_left(arr, 5))   # 2
print(bisect.bisect_right(arr, 5))  # 4

left：返回第一个等于 x 的索引（如果存在）
right：返回最后一个等于 x 的索引 + 1

# 将降序转为升序（取负数）
arr = [9, 7, 5, 3, 1]
arr_neg = [-x for x in arr]  # [-9, -7, -5, -3, -1]
