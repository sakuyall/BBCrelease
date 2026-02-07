"""2/6/26
将本题理解后结合bisect重新传
二分找出战力小于目标的个数, 接着减去其中有矛盾的个数
"""
import sys
import bisect

def conf_counts(n, lir, conf):
    total = [[] for _ in range(n+1)]
    # 在对应下标列表中储存矛盾对象
    for x, y in conf:
        total[x].append(y)
        total[y].append(x)
    
    count_list = []
    for i in range(1, n+1):
        counts = 0
        for j in total[i]:
            # 依次比对目标下标 与 其矛盾对象下标 的战力大小
            if lir[i] > lir[j]:
                counts += 1
        count_list.append(counts)
        
    return count_list
    
n, k = map(int, input().split())       # n k
lir = list(map(int, input().split()))  # 战力列表r
lir.insert(0, 0)                       # 开头放个0调整序号
conf = []                              # 矛盾列表

for _ in range(k):
    conf.append(tuple(map(int, input().split())))
lis = sorted(lir[1:])                  # 战力列表排序

# 获取矛盾数列表
count_list = conf_counts(n, lir, conf)

# 获取二分结果列表
flag = 0
result_list = []
for target in lir[1:]:                      # target表示原战力列表元素
    bs = bisect.bisect_left(lis, target)    # 当前角色战力大于几个
    res = bs - count_list[flag]             # 结果为二分结果减去其中小于它的矛盾数
    result_list.append(res)
    flag += 1                               # 用flag标识, 不要与target弄混

# 解包输出
print(*result_list)