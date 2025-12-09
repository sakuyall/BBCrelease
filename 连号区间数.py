"""12/9/25
输入: 第一行数目N 第二行n个数
输出: 一个整数表示不同区间数目

单个数字自身会成为一个可行区间, 不用判断
用切片把原列表切出各种长度的列表
判断排序后的数列为连续自然数
1)把列表转换为集合, 判断长度变化, 是否有重复元素
2)判断列表 最大值 - 最小值 是否等于 列表长度-1
因为在元素不重复的情况下, 如果不满足2)就说明数列缺项

本题因为是排列, 所以原列表默认为连续数列
"""
# 这个是考虑排序时做的, 超时
def check(li):
    # 传入为原列表切片
    setlist = set(li)
    if len(setlist) == len(li):
        if max(li) - min(li) + 1 == len(li):
            # 同时满足两个检查条件, 返回True
            return True
    return False

def main():
    # 数据处理
    N = int(input())
    li_p = list(map(int, input().split()))

    counts = 0                  # 满足条件的数量
    for left in range(N):
        for right in range(left, N):
            # 获取子序列, 注意切片不包含右界所以要加1
            temp = li_p[left : right+1]

            if left == right:
                # 判断单个元素直接加1次数
                counts += 1
                continue
            else:
                if check(temp):
                    # 满足条件的长列表加1次数
                    counts += 1
    print(counts)
if __name__ == "__main__":
    main()

# 优化后这个双指针思路要记住
"""
输入: 第一行数目N 第二行n个数
输出: 一个整数表示不同区间数目

因为题中给出的排列, 元素不重复
如果不满足判断条件就说明切出的子序列内数字不连续

获取各种长度的列表(实际上为了优化没有创建新列表)
判断列表 最大值-最小值+1 是否等于 元素个数·······························(1)
满足条件则说明是连号区间
left与right分别为原列表的两个索引, 两索引之间元素个数为right-left+1······(2)

所以总的来说判断条件就是:
    最大值-最小值 == right-left

3   4   2   5   1
L           R
此时5-2 == 3-0
"""
def main():
    N = int(input())
    li_p = list(map(int, input().split()))
    
    counts = 0
    
    for left in range(N):
        # 左索引移动后初始化最小值和最大值
        min_val = li_p[left]
        max_val = li_p[left]
        
        for right in range(left, N):
            # 更新最小值和最大值, 每扩容区间就比较一次
            min_val = min(min_val, li_p[right])
            max_val = max(max_val, li_p[right])

            if max_val - min_val == right - left:
                counts += 1

    print(counts)

if __name__ == "__main__":
    main()