"""11/30/25
分糖果
"""
def game(n, li):
    plus = 0
    while len(set(li)) != 1:
        cost = [_ // 2 for _ in li]   # 创建出分出一半的列表,防止干扰数据
        li = [_ // 2 for _ in li]     # 原值分完变为原来一半
        cost.append(cost.pop(0))      # 第一位移动到最后一位实现给前一个人
        result = [li[_] + cost[_] for _ in range(len(li))]
        
        for i in range(n):
            if result[i] % 2 != 0:
                result[i] += 1        # 上面一轮游戏过后,为奇数的糖数加1
                plus += 1             # 记录补充数
        li = [j for j in result]
        
    return plus

n = int(input())
candy = list(map(int, input().split()))
print(game(n, candy))