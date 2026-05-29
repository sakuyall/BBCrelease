"""5/26/26
排列问题DFS
"""
# 独立写一次, node似乎在排列中是用不到的
def dfs(node, cnt):
    if cnt == n:
        print(*ans)
        return
    
    for i in range(1, n + 1):
        if not used[i]:
            ans.append(i)
            used[i] = True
            
            dfs(i, cnt + 1)

            ans.pop()
            used[i] = False


n = int(input())
ans = []
used = [False] * (n + 1)

dfs(0, 0)
