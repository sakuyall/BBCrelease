"""1/27/26
套餐设定后需要全部保持一样, 样例三因为没有重样所以只能一份
设能制作x个套餐, x最少为0, 最多为100库存少于要求返回0

贪心首先锚定列表前n个作为套餐组合
检查制作套餐消耗与库存拥有的单种食物量
使单个套餐量达到n为合格
"""
from collections import Counter
# Counter()会将一个可迭代对象转换成类似字典的结构, 键是元素本身, 值是该元素出现的次数

n, m = map(int, input().split())       # 打包任意n个, 库存m个
li = list(map(int, input().split()))   # 各是什么种类
cnt = Counter(li)

if m < n:      # 存货不足, 无法搭配
    print(0)
    exit()

left, right = 0, 100
while left <= right:
    mid = (left + right) // 2
    
    if mid == 0:
        # mid=0总是可行的，尝试更大的值
        left = mid + 1
        continue  # 跳过下面的计算
    
    counts = 0
    for i in cnt.values():        # 遍历每种食物的数量
        counts += i // mid        # 累加每个套餐最多能从该种类拿几个
    if counts >= n:               # 大于n时满足条件
        left = mid + 1
    else:
        right = mid - 1
        
print(right)