"""5/14/26
区别在于一维01背包遍历背包容量是倒序
完全背包是正序
"""
n, m = map(int, input().split())
dp = [0] * (m + 1)

for _ in range(n):
    v, w = map(int, input().split())
    for j in range(v, m + 1):
        dp[j] = max(dp[j], dp[j - v] + w)

print(dp[m])
