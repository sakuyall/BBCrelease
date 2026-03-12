"""3/12/26
用变量target跟踪当前期望匹配的值，初始为K

然后遍历数组每个元素，如果当前元素等于target，则target减1
当target变为0时说明找到一个完整K倒计数，计数加1并重置target为k

如果当前元素不等于target, 则判断当前元素是否等于k
若等于K则设置target为K-1以开始新的匹配，否则重置target为K等待下一次匹配
"""
# 数据处理
t = int(input())
for _ in range(1, t + 1):    # 题中要求的从1开始编号
    n, k = map(int, input().split())
    li = list(map(int, input().split()))

    counts, target = 0, k
    for i in li:
        if i == target:
            # 匹配
            target -= 1
            if target == 0:
                # 减到0说明刚完成了结尾数字1的匹配, 计数并还原
                counts += 1
                target = k
        else:
            # 不匹配
            if i == k:
                # 可能会开始下一个子序列
                target = k - 1
            else:
                # 初始化
                target = k

    print(f"Case #{_}: {counts}")