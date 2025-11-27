"""11/27/25
训练士兵
    ----排序加贪心
    单独一个人的价格为p,次数为c
    输入人数n 团建价格S
    先选次数少的一起团建,然后每次都比较团建和单独费用
"""
n, S = map(int, input().split())
solider = [list(map(int, input().split())) for _ in range(n)]

solider.sort(key = lambda x: x[1], reverse = True)
# 接收列表内元素并返回其[1]位置,倒序排列方便pop
team, money = 0, 0
isolate = sum(p for p, c in solider)  # 剩余人数单练一次费用
while solider:
    pp, cc = solider.pop()         # 注意这里把最后一个人拿出去了
    if isolate > S: # 团购
        money += S * (cc - team)   # 按剩余最少次数的人进行团购,已经团购过的减去以前的次数就是剩余次数
        team = cc  # 记录团购次数
    else: # 单练
        money += pp * (cc - team)  # 单价乘以剩余次数

    isolate -= pp                  # 执行一次后,单练价格去掉这个练完的
    
print(money)