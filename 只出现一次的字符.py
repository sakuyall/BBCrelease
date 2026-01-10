dic = {}
s = str(input())
for ch in s:           # 遍历该字符串
    dic[ch] = dic.get(ch, 0) + 1   # 该值 = 键对应值(没有建立为0) + 1
    
for ch in s:
    if dic[ch] == 1:
        print(ch)
        exit()         # 找到值为1的直接结束程序
        
print("no")