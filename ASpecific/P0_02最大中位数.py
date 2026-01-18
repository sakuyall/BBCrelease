"""1/18/26
二分的特点似乎是向着目标答案的x来进行讨论多一点或少一点的情况
假定中位数达到x, 也就是说中位数及其以后的数至少都是x
接着检查k次操作能否将后边的全补充到x(填坑)
计算后边小于x的数填坑的次数counts是否小于等于操作数k
最后输出最大满足条件的x

x边界: [当前中位数, 当前中位数+k], 当前中位数下标为n//2
这一过程, x越大, 需要填坑次数counts越多, 单调不减, 需要注意比大小的方向
"""
def count(li, x):
    counts = 0
    for i in li[n // 2:]:           # 为坑的部分加上填坑次数
        if i < x:
            counts += x - i
            
    return counts

n, k = map(int, input().split())          # 列表长度, 操作数
li = list(map(int, input().split()))      # 获取列表
li_s = sorted(li)                         # 先进行排序

# 这是中位数x的取值范围
left = li_s[n // 2]         # 左边界
right = left + k            # 右边界, 或者直接取最大值1000000000
ans = left                  # 初值设定为原本中位数
while left <= right:
    mid = (left + right) // 2
    counts = count(li_s, mid)
    if counts <= k:                       # 说明次数够用, x可以取更大, 在右半找
        ans = mid                         # 储存当前结果
        left = mid + 1
    else:
        right = mid - 1                   # x过大, 往回找左半
    
print(ans)