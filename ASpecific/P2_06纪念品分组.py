"""3/7/26
使最大的和小的配对, 若仍超过w则说明最大的只能自己一组, 右侧排出最大数
两者组合成一对时, 指针同时移动, 并记录组队次数
"""
w = int(input())
n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li.sort()      # 先排序

i , j = 0, n - 1         # 指针置于列表收尾, 向中间收缩
single, double = 0, 0    # 单个一组数量, 两个一组数量

while i < j:
    if li[i] + li[j] > w:
        j -= 1
        single += 1
    else:
        i += 1
        j -= 1
        double += 1
        
if i <= j:      # 三个数配对后剩一个, 或两个数无法配对, 导致最后指针在一起的情况
    single += 1 # 因为如果最后两个数刚好配对, 那么ij指针会交错过去的, 不能算这种情况

print(single + double)