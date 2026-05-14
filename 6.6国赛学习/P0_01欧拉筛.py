def linear_sieve(n):
    """
    线性筛（欧拉筛） O(n) 时间复杂度
    核心：每个合数只被其最小质因子筛掉一次
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0和1不是质数
    primes = []

    for i in range(2, n + 1):
        # 若为质数则加入列表
        if is_prime[i]:
            primes.append(i)

        # 用当前 i 与已找到质数相乘
        for p in primes:
            # 若超过查找范围直接跳出
            if i * p > n:
                break
            
            # 标记 i*p 为合数
            is_prime[i * p] = False

            # 核心优化：如果 p 是 i 的最小质因子，则 break
            # 保证每个合数只被最小质因子筛掉，达到 O(n)
            if i % p == 0:
                break

    return primes, is_prime

n = 100
primes, is_prime = linear_sieve(n)

print(primes)
print(is_prime[59])
