"""1/17/26
假设切出的巧克力边长为x, 对于某块H * W的巧克力, 可以切出(H//x) * (W//x)块边长x的
把每块巧克力切出的加一起总和为count, count要大于等于人数K

在这一过程中, 边长x设定的越大, 结果count就会越小(至少是不会增加的)
count视为x的函数的话, 函数count(x)是单调不增的
于是可以使用二分从小到大查找出一个满足条件的x
题中给定1 <= x <= 10 ** 5作为查找范围
"""
def count(li, x):
    counts = 0
    for i in li:
        counts += (i[0] // x) * (i[1] // x)
    return counts
    
n, k = map(int, input().split())                         # 数据组数, 人数
li = [list(map(int, input().split())) for _ in range(n)] # 储存形如[[6, 5], [5, 6]]二维列表

left, right = 1, 100000
result = 1                     # 设定至少输出结果是1
while left <= right:
    mid = (left + right) // 2
    if count(li, mid) >= k:    # 当前x可行, 记录并尝试更大的x, 取右半
        result = mid
        left = mid + 1
    else:                      # 当前x太大, 尝试更小的, 取左半
        right = mid - 1
        
print(result)

# 对比左闭右开区间写法
"""
left, right = 1, 100001        # 表示区间 [1, 100001)，实际检查 1~100000
while left < right:            # 左闭右开 左<右时继续
    mid = (left + right) // 2
    if count(li, mid) >= k:
        left = mid + 1         # 可行, 在 [mid+1, right) 继续
    else:
        right = mid            # 不可行, 在 [left, mid) 继续
        
print(left - 1)                # 因为退出时 left 是第一个不可行的，所以答案 left-1
"""