"""二分查找1/16/26
一些思路:
    题目测试点巨大, 应使用nlogn情况, 可能会应用二分
    找到欲求解x, x相关的函数(单调的)
    边界问题, 初值与封顶
    注意判别方向
    目前采用闭区间写法 l<=r 条件

基本步骤:
    问题转化, x选取
    x边界设定
    检查函数计算方法与单调性
    确定"第一个"和"最后一个"判断要求
    码二分模板

定义基本二分函数
同时做题, 争取不思考下标构建直接写出
学习bisect库使用

记下一些模板的想法:
    边界的处理规则都要根据区间本身的定义来写, 循环开始的right要注意是len()还是len()+1
    关于左闭右开和左闭右闭, 举个例子, 对于[1, 1]这个区间能不能取到left <= right, 当然可以这么写
    同样, 如果是开区间[1, 1)这么写, 到底是包含还是不包含1? 所以此时left与right不能取等于

    接着, 闭区间已经判断mid位置不满足条件, 所以下一次区间变换, 因此要取mid+-1, 不然容易死循环
    最后可以像ds模板那样预设初值写法, 或者最后返回mid位置, 若都没有找到则返回None
    而开区间判断不包含mid位置, 所以下一次right开区间要取mid作为边界, 而左边界由于是闭区间要取mid+1


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