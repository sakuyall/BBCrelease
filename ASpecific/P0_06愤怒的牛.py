"""1/23/26
设最小距离x, counts表示牛的数量
x越大counts越小, 单调不增
最多情况n=m,距离为0
最少情况距离10**9
计算在某x情况下最多放下多少牛
m头牛把区间分为m-1段, 当一段长度达到x或加上下一小块超过x, 则开始下一段
"""
def count(li_s, x):
    counts = 1           # 第一个位置先放牛
    last = li_s[0]
    for i in range(1, len(li_s)):
        if li_s[i] - last >= x:   # 在这位置放牛
            counts += 1
            last = li_s[i]        # 更新基底
        # 不然就继续加直到距离大于等于x
    return counts        # 返回牛数

n, m = map(int, input().split())  # n间, 牛m
# li = list(map(int, input().split()))   # 这是用空格隔开的处理, 题中说用空格分隔
li = [int(input()) for _ in range(n)]    # 这是按行隔开的处理, 但提交后测试不知为何是按行输入的...
li_s = sorted(li)

left, right = 0, 1000000000
ans = left
while left <= right:
    mid = (left + right) // 2
    counts = count(li_s, mid)
    if counts >= m:            # 当前放牛数大于m, 向右寻找更小
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)