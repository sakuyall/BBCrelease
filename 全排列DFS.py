"""1/16/26
深度优先搜索
"""
n = int(input())
path = []                 # 当前排列
used = [False] * (n + 1)  # 标记数字是否使用过

def dfs():
    # 如果路径长度等于n, 说明找到一个完整排列
    if len(path) == n:
        print(' '.join(map(str, path)))
        return
    
    # 尝试每个数字
    for i in range(1, n + 1):
        if not used[i]:
            # 选择i
            used[i] = True
            path.append(i)
            
            # 递归
            dfs()
            
            # 回溯, 撤销选择
            path.pop()
            used[i] = False
    
dfs()