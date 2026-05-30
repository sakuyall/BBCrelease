"""5/30/26
题目有些偏颇
并不是在说如何建立与维护非对称二叉树
本题的背景是计算有多少棵不同的非对称二叉树
而且由于四重循环, 仅能在小数据范围下通过
感觉意义不大, 权当锻炼dp思维
"""
n, k = map(int, input().split())
# dp[node][h]代表有node个节点情况下, 该树高度为h, 满足的条件数
# 这里因为给出参数较少, 所以往大了扩也是可以的
dp = [[0] * (n + 1) for _ in range(n + 1)]

# 初始条件, 空树满足公式, 因此条件数也为1
# 初始化的列表其余为0就是不存在的情况
dp[0][0], dp[1][1] = 1, 1

for total in range(2, n + 1):
    # 之前定义了01情况, 接着从总节点数2个节点开始遍历
    for left in range(0, total):
        # 左子节点数的取值范围为0到total-1, 因为有一个是根节点
        # 右子节点数可以直接计算
        right = total - left - 1
        for hl in range(0, left + 1):
            # 对于根节点而言, 左子树的高度可以由左子节点数获取
            # 最大可以取到左子节点数, 右子节点同理
            for hr in range(0, right + 1):
                if max(hl, hr) >= k * min(hl, hr):
                    # 子树高度加1为父树高度
                    h = max(hl, hr) + 1
                    dp[total][h] += dp[left][hl] * dp[right][hr]

# 输出节点数为n全部高度, 满足的条件数
print(sum(dp[n]))
