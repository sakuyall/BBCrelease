import sys

def binary_count_lower(sorted_values, target_value):
    """返回严格小于target_value的元素个数"""
    left, right = 0, len(sorted_values) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_values[mid] < target_value:
            left = mid + 1    # 继续向右找
        else:
            right = mid - 1   # 向左找
            
    return left

def conflict_lowers(conflicts, values, n):
    """一次性预计算所有战士的低战斗力矛盾对手数量"""
    # 构建邻接表
    adj = [[] for _ in range(n + 1)]
    for x, y in conflicts:
        adj[x].append(y)
        adj[y].append(x)
    
    # 计算结果
    conflict_lowers_list = [0] * (n + 1)  # 换个变量名避免冲突
    for i in range(1, n + 1):
        count = 0
        for neighbor in adj[i]:
            if values[neighbor] < values[i]:
                count += 1
        conflict_lowers_list[i] = count
    
    return conflict_lowers_list

# 数据处理
data = sys.stdin.read().strip().split()
it = iter(data)
n = int(next(it))
k = int(next(it))

# 读取战斗力, 战士编号从1开始, 列表长度设为n+1, 索引0不使用
values = [0] * (n + 1)
for i in range(1, n + 1):
    values[i] = int(next(it))

# 读取矛盾关系
conflicts = []
for _ in range(k):
    x = int(next(it))
    y = int(next(it))
    conflicts.append((x, y))

# 对原列表排序, 不包括索引0位置
sorted_values = sorted(values[1:])

# 预处理：一次性计算所有战士的低战斗力矛盾对手数量
conflict_lower_counts = conflict_lowers(conflicts, values, n)

results = []
for target in range(1, n + 1):
    target_value = values[target]

    # 比它power小的个数
    count_lower_res = binary_count_lower(sorted_values, target_value)

    # 直接使用预处理结果，O(1)时间获取
    conflicts_lower_res = conflict_lower_counts[target]
    
    result = count_lower_res - conflicts_lower_res
    results.append(str(result))
    
print(" ".join(results))