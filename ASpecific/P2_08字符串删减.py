"""3/8/26
感觉比较难解决的就是 字符串越界, 以及结尾位置满足条件的漏加
没有多少天了已经
"""

n = int(input())
s = str(input())

if n < 3:   # 字符串长度小于3不需要删除
    print(0)
    exit()

i= 0
counts, length = 0, 0

while i < n:
    if s[i] != "x":
        # 跳过不为x的部分
        i += 1
        continue    # 避免一起执行下边代码
        
    # 此时部署ij在x串的第一个x上
    j = i

    # 找出一段连续的x串
    while j < n and s[j] == "x":
        # 满足条件时扩张窗口
        j += 1

    # j的下一位置非x说明此x串结束，记录x串长度
    length = j - i        
    if length > 2:
        # 以上判断结束后, x串长度大于2则计数
        counts += length - 2

    # 最后更新i的位置到新一个不为x处
    i = j

print(counts)