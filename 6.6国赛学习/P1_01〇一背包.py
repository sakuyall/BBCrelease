"""5/13/26
"""
n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]  # n行m列二维列表

for i in range(1, n + 1):
    # dp[i][j]表示 前i个物品在容量不超过j时的最大价值
    v, w = map(int, input().split())
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= v:
            # 要么保持原状, 不添加新物品
            # 要么回退到上一个物品状态
            dp[i][j] = max(dp[i][j], dp[i - 1][j - v] + w)

print(dp[n][m])


# 一维优化
n, m = map(int,input().split())
dp = [0] * (m + 1)

for _ in range(n):
    v, w = map(int,input().split())
    for j in range(m, v - 1, -1):
        dp[j] = max(dp[j], dp[j - v] + w)

print(dp[m])
