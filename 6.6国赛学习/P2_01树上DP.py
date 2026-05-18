"""5/18/26
没有上司的舞会
模板题, DFS后序遍历+树形DP+邻接表
"""
import sys, os
sys.setrecursionlimit(100000)    # 扩展最大递归深度

def dfs(u):
    # 设置该节点初始值, 之后往上加
    dp[u][0] = 0
    dp[u][1] = h[u]

    if not g[u]:           # 递归到叶子节点时
        return             # 显式终止, 其实叶子节点在for循环中没有值会自己跳出

    for child in g[u]:
        # 依次遍历该节点u的子节点
        dfs(child)
        # 转移方程如下,不选此节点则子节点随意取最大值, 选取此节点则不能选子节点
        dp[u][0] += max(dp[child][0], dp[child][1])
        dp[u][1] += dp[child][0]


n = int(input())
h = [0] + list(map(int, input().split()))
g = [[] for _ in range(n + 1)]     # 邻接表, 一维列表, 只能向下寻找
has_parent = [False] * (n + 1)     # 储存是否有父节点

for _ in range(n - 1):
    # 建树, dfs只读不写
    a, b = map(int, input().split())
    g[b].append(a)          # 将下属添加到他的上司列表中
    has_parent[a] = True    # 标记有父节点

# 找根节点
root = 1
for r in range(1, n + 1):
    if not has_parent[r]:
        root = r
        break

# dp[u][0]表示不选节点u的最大快乐值, [1]则表示选此节点后的最大快乐值
dp = [[0, 0] for _ in range(n + 1)]
dfs(root)

print(max(dp[root][0], dp[root][1]))
