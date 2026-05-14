"""5/14/26
可以摊开按照01直接硬算
以下按照二进制优化算算法为ologn
"""
n, m = map(int, input().split())
dp = [0] * (m + 1)

for _ in range(n):
    v, w, c = map(int, input().split())
    # 体积 价值 次数限制

    k = 1
    while c >= k:
        # 放入k这一堆物品包
        for j in range(m, v * k - 1, -1):
            dp[j] = max(dp[j], dp[j - v * k] + w * k)

        # 从次数中减去装进去的这份, 然后打包出下一堆k
        c -= k
        k <<= 1
    
    # 兜底, 最后没办法减k后, 剩余的打为一包
    if c > 0:
        for j in range(m, v * c - 1, -1):
            dp[j] = max(dp[j], dp[j - v * c] + w * c)

print(dp[m])
