"""1/26/26
n个怪, 每个防御为ai, 初始法力为m, 每次消耗x点最多同时打两个, x >= ai就会消灭, 找出k最大值
通过合理安排攻击, 可以将第 1∼k个怪兽全部消灭, 拿样例1分析:
5 7  
2 3 5 4 1
有7点法力, 先用五点消灭3和5, 再用两点消灭开头的2, 这样能实现第1-3个全部消灭, 所以k是3
但最终状态必须是: 编号1到k的怪兽全部死亡, 编号k+1及以后的怪兽可能死亡也可能活着(不影响问题)

考虑贪心, 锚定前k个数, 将其中最大的与次大的配对消灭, 第三大的与第四大的配对消灭, 等等
将以上组对的最大值依次相加返回为counts, k越大counts越大, 满足单调函数, 可用二分
k从1开始满足条件, 找最大的k, 使消耗法力count(k)小于等于m
"""
def count(li, k):
    counts = 0
    li_slice = li[:k]                          # 切出0到k-1, 也就是编号1到k的怪
    li_sort = sorted(li_slice, reverse = True) # 对该切片反转排序
    
    for i in range(0, k-1, 2):                 # k为7遍历0 2 4
        counts += max(li_sort[i], li_sort[i + 1])
    if k % 2 == 1:                             # k为奇就额外补上最后一个数
        counts += li_sort[-1]
        
    return counts
"""# 或者这样写, 024位置已经是所在组对中最大值
def count(li, k):
    li_slice = li[:k]
    li_sort = sorted(li_slice, reverse=True)
    return sum(li_sort[0::2])    
"""
n, m = map(int, input().split())  # 怪数, 法力
li = list(map(int, input().split()))

left, right = 1, n                # n个怪
while left <= right:
    mid = (left + right) // 2
    counts = count(li, mid)
    if counts <= m:               # 目标在右半, 继续增大k使满足的counts接近m
        left = mid + 1
    else:                         # 目标在左半
        right = mid - 1
        
print(right)