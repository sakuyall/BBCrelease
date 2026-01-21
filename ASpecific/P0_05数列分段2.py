"""1/21/26
设最大值为x, 输入序列为li
操作后x最小为max(li), 最大为sum(li), 分别设为left与right
当最大值为x时, 一般x越大段数count(x)越小, 属于单调不增
检查段数count(x)是否小于等于m
分段过程中, 若单个区间加和小于等于预定x, 则认定该次扩充, 否则不扩充此数并从这里分段
分段的次数加1返回为段数count(x)
"""
def count(li, x):
    counts = 1
    add = 0
    for i in range(len(li)):
        if li[i] > x:            # 若该数本身已经大于x, 则返回一个大于m的数表示无法分段
            return 100000000
            
        if add + li[i] > x:      # 加下一个数大于x则分段, 下一次以它为基底开始
            counts += 1          # 前边判断过li[i]保证此数是小于x的
            add = li[i]
        else:                    # 未超过则扩充该数
            add += li[i]

    return counts

n, m = map(int, input().split())
li = list(map(int, input().split()))

left, right = 1, 1000000010
ans = left
while left <= right:
    mid = (left + right) // 2
    counts = count(li, mid)
    if counts <= m:              # 尝试更小x来增大counts, 往左半找
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
        
print(ans)