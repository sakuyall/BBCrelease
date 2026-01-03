"""1/2/25
传统递归效率过低, 使用lru_cache装饰器自动缓存结果
"""
from functools import lru_cache

@lru_cache(maxsize=None)   # 缓存大小不限制
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def main():
    n = int(input())
    for i in range(n):
        print(fib(i), end = " ")

if __name__ == "__main__":
    main()

# 以下另一种非常简化的解法, 值得记忆
p, q = 0, 1
for _ in range(int(input())):
    print(p, end=' ')
    p, q = q, p + q
# 不过这个最后会多一个空格, 可以使用.rstrip()删除结尾不可见字符