"""5/29/26
这是最长公共子序列LCS模板题目
使用dp进行求解
注意初始状态及转移方程寻找
另外
越界时检查列表是否建错了
"""

import sys, io

# data = "\
# 5 6\n\
# 1 2 3 4 5\n\
# 2 3 2 1 4 5"
# sys.stdin = io.StringIO(data)

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
# dp[i][j]表示a的前i个与b的前j个最大公共序列长度
# 所以ab要1-based

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])
