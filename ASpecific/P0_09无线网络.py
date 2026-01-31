"""1/31/26
对奶牛位置排序(基站随意放置不会影响)
寻找半径为r满足题中覆盖要求
贪心, 当前奶牛有序, 将基站放在靠前且未被覆盖的奶牛位置+r处, 接着向后找未被覆盖的重复此操作
检查是否全部覆盖, 所以前边不用去重
考虑存在浮点数不能使用range()判断, 并且使用浮点二分
"""
import sys

def setting(pos_s, r):
    """
    输入排序后的列表, 查找半径
    输出是否可行布尔值, 以及可能的坐标列表
    """
    s, i = [-r], 0                  # 基站坐标列表, 不需要三个就可以满足时默认放在0处
    for each in pos_s:
        if  each > s[i] + r:        # 大于上一个的右边界未被覆盖时(使用123下标储存最终位置)
            if i == 3:              # 已有三个基站无法满足要求, 退出, 防止列表越界
                return False, []
            s.append(each + r)      # 未被覆盖的插基站
            i += 1                  # 放下一个
    while len(s) < 4:
        s.append(pos_s[-1])    # 少于三个坐标补全
            
    return True, s[1:]         # 满足要求返回三个坐标

data = sys.stdin.read().strip().split()
it = iter(data)
# 尝试使用sys库读取输入并用迭代器赋值
n = int(next(it))
positions = [int(next(it)) for _ in range(n)]
pos_s = sorted(positions)      # 正序排列

# 浮点二分而非整数二分
left, right = 0.0, float(pos_s[-1] - pos_s[0])  # 设为浮点数
eps = 1e-6                     # 精度给定
while right - left > eps:
    mid = (left + right) / 2
    is_access, answer = setting(pos_s, mid)     # 获取函数返回值
    if is_access:              # 满足条件往左找
        right = mid
    else:                      # 不满足往右找
        left = mid
        
last_access, last_ans = setting(pos_s, right)   # 最终坐标
print(f"{right:.6f}")   # 格式化输出查找结果与对应坐标
print(f"{last_ans[0]:.6f} {last_ans[1]:.6f} {last_ans[2]:.6f}")