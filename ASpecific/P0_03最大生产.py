"""1/18/26
生产x个机器需要每种零件数为x * ai, 当前该零件库存为bi
以上两者的差 x * ai - bi 整体求和不能超过万能件k的数量
x范围左边界设定为0, 右边界全都取最大值, 设定为(b[0] + k) / a[0] = (1e9 + 1e9) / 1 = 2e9
"""
def count(li_a, li_b, x):
    counts = 0
    for _ in range(len(li_a)):
        temp = li_a[_] * x - li_b[_]    
        if temp > 0:
            counts += temp          # 注意temp为负时不计入, 因为不同零件不通用
    return counts

n, k = map(int, input().split())    # n种零件, k个万能
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))

# x边界设定
ans = 0                             # 初值设为0
left, right = 0, 2 * 10**9 + 10     # 加10或者别的缓冲确保完全大于右边界
while left <= right:
    mid = (left + right) // 2
    counts = count(li_a, li_b, mid)
    if counts <= k:
        ans = mid
        left = mid + 1              # 这时尝试寻找更大x, 找右半
    else:
        right = mid - 1

print(ans)