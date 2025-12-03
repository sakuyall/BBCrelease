"""12/1-3/25
日志统计
"""
"""
起初ji位于相同位置,随后i不断右移
i再次右移直到超过跨度d,此时跨度为d+1
执行排除,j左移将跨度缩回d
之后不断执行前两步,直到i遍历结束range的n-1位置循环终止
"""
# 数据处理
n, d, k = map(int, input().split())   # 帖子数, 时间范围, 赞数标准
log = [list(map(int, input().split())) for _ in range(n)]  # 时刻, id名

# 按照时间顺序进行排序,统计该既定时间段内各帖子获得条目数量
log.sort(key = lambda x: x[0])
id_count = {}   # 使用字典储存帖子点赞次数
result = set()  # 集合存储热帖ID

# 双指针 i是右边界,j是左边界
j = 0                                          # 左边界放在开头,右边界右移
for i in range(n):
    ts_i, id_i = log[i]                        # 获取当前条目 时间,id
    id_count[id_i] = id_count.get(id_i, 0) + 1
    # //这个方法要记住
    # 键id_i的新字典值为获取原字典值 (get函数没有默认为0)加1
    
    while j < i and ts_i - log[j][0] >= d:     # 当前时间与左边界跨度超过d就执行排除
        ts_j, id_j = log[j]                    # 获取即将移出窗口(左边界)的点赞记录
        id_count[id_j] -= 1                    # 将该帖子的点赞数减1
        if id_count[id_j] == 0:
            del id_count[id_j]                 # 如果计数为0，删除该键节省空间
        j += 1                                 # 左边界右移
    
    # 检查当前帖子是否成为热帖
    if id_count[id_i] >= k:                    # 值大于等于标准k时
        result.add(id_i)                       # 将此id保存于集合防重复

# 从小到大的顺序输出热帖id
for post in sorted(result):
    print(post)