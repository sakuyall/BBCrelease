"""二分查找1/16/26
定义基本二分函数
同时做题, 争取不思考下标构建直接写出
学习bisect库使用

# 建议 掌握一种模板记住即可
P0_01有开区间与闭区间区别对比
"""
# 二分查找(Binary Search)  引自Algorithm
# 排序后一半一半查找,减少了查找次数
def BinarySearch(li, search):
    left = 0
    right = len(li) - 1
    while left <= right:
        # 若候选区仍有值
        mid = (left + right) // 2
        if li[mid] == search:
            # 如果找到search了直接返回下标
            return mid
        elif li[mid] > search:
            # search在左边,右半区域舍去
            right = mid - 1
        else:
            # search在右边
            left = mid + 1
    # 还有找不到的情况
    else:
        return None
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(BinarySearch(li, 3))
# 由于循环在不断减半,所以复杂度为logn


# 流程模板伪代码  引自五点七边
"""
l = -1, r = N
while l + 1 != r:         # 划分蓝红区域在, 确定isblue条件
    m = (l + r) // 2
    if isblue(m):
        l = m
    else:
        r = m
return l or r             # 确定返回l还是r
                          # 根据实际情况再加入后处理逻辑
"""

# python经典模板
"""
left = 1, right = max_size
while left < right:
    mid = (left + right + 1) // 2  # 上取整，避免死循环
    if count(mid) >= K:
        left = mid
    else:
        right = mid - 1
"""