"""3/4/26
多锻炼思路, 先考虑特例, 函数不要挖坑
"""
def check(s):
    # 遍历每个A计算它右侧P的个数
    li = []
    counts = 0
    for ran in s:
        if ran == "A":
            li.append(counts)    # 再次检测到A返回上一串价值并重置
            counts = 0
        if ran == "P":
            counts += 1
    if 'A' in s:
        li.append(counts)        # 循环结束后添加最后一个A右边的P个数
    else:
        return [0]    # 字符串不存在A直接返回0, 防止空列表使用max报错
        
    return li[1:]     # 排除掉第一次加入的无关P
    
def main():
    # 数据处理
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = str(input())
        print(max(check(s)))

if __name__ == "__main__":
    main()