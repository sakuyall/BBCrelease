"""5/26/26
组合问题DFS
"""
# 独立完成一次, 应注意node的起始位置, 模拟输出来观察
def dfs(node, cnt):
    if cnt + n - node < m:
        # 剪枝
        return

    if cnt == m:
        # 已选m个则结束
        print(*ans)
        return
    
    for nex in range(node + 1, n + 1):
        ans.append(nex)
        dfs(nex, cnt + 1)
        ans.pop()


n, m = map(int, input().split())
ans = []
dfs(0, 0)
