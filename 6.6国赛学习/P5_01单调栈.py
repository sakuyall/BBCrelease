"""5/28/26
单调栈的例题, 看了很多资料, 目前未遇到等于情况如何判别
"""
# 整体采用1下标方法, 注意输出时把0位置排除
n = int(input())
h = [0] + list(map(int, input().split()))

# 不存在输出-1, 直接初始化为-1
left_res = [-1] * (n+1)
right_res = [-1] * (n+1)

stack = []
for i in range(1, n + 1):
    while stack and h[ stack[-1] ] <= h[i]:
        # 循环弹出前边所有矮的, 因为新加入的较大
        # 后续不会用到这几个矮的了
        stack.pop()

    if stack:
        # 栈不空时进行赋值, 栈空不赋值, 因为左侧不存在更高的
        left_res[i] = stack[-1]

    stack.append(i)    # 最后入栈当前元素

# 一下另一方向同理
# 需要注意的是逆序遍历, 以及j不要写成i
stack = []
for j in range(n, -1, -1):
    while stack and h[ stack[-1] ] <= h[j]:
        stack.pop()
    if stack:
        right_res[j] = stack[-1]
    stack.append(j)

# 切除0元素解包输出
print(*left_res[1:])
print(*right_res[1:])
