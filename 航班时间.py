"""12/7/25
输入第一行为一个正整数T, 表示输入数据组数
每组数据包含两行, 第一行为去程的起降时间, 第二行为回程的起降时间

题目中说来去时间是一样的, 因此算出每次的时间加起来除以2肯定是实际路程的时间, 这样时区的影响就被抵消了
对求同一天两组数据各自的差值, 将结果相加抵消时差后再/2就是飞行时间
判断是否存在+1情况,列表roundtrip中子列表长度若为3,则判断子列表[2]位置是什么
"""
from datetime import datetime

def timediff(roundtrip):
    # 起飞时间与降落时间
    # 接收的列表形式为[['10:19:19', '20:41:24'], ['22:19:04', '16:41:09', '(+1)']]
    different = []
    for i in range(2):
        # 转换为datetime.time格式化
        time1 = datetime.strptime(roundtrip[i][0], "%H:%M:%S")
        time2 = datetime.strptime(roundtrip[i][1], "%H:%M:%S")
        time_diff = (time2 - time1).total_seconds()  # 基础时间差
        # 注意若t2<t1, 输出.seconds秒数是正数: -1 day, 23:00:00
        # 应使用.total_seconds()
        
        if len(roundtrip[i]) == 3:
            if roundtrip[i][2] == "(+1)":
                time_diff += 24 * 3600  # 过一天加24h
            elif roundtrip[i][2] == "(+2)":
                time_diff += 48 * 3600  # 过两天加48h
        
        different.append(time_diff)
    
    # 求得航班时间(秒数)的平均值
    flight_seconds = (different[0] + different[1]) / 2
    hours = int(flight_seconds // 3600)
    minutes = int((flight_seconds % 3600) // 60)
    seconds = int(flight_seconds % 60)
    
    # 格式化为两位数
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def main():
    T = int(input())
    for i in range(T):
        roundtrip = []
        for j in range(2):
            tl = list(map(str, input().split()))
            roundtrip.append(tl)
        print(timediff(roundtrip))

if __name__ == "__main__":
    main()

# 想了不用库的方法, 可以这么写, 灵感来自字符串笔记
def timediff(li):
    # 接收列表类型是这样的['17:48:19 21:57:24']
    table = li[0].split(" ")  # 把两时间分开, 若有(+1)则列表长度为3
    sec2 = []                 # 储存起飞降落时间秒数
    
    for _ in range(2):
        hms = table[_].split(":")   # 这里这么做是因为table第三个元素(+1)不能int
        sec2.append(int(hms[0])*3600 + int(hms[1])*60 + int(hms[2]))  # 计算总秒数
    time_diff = sec2[1] - sec2[0]   # 起飞降落的秒数差, 作为一个基础结果
    
    if len(table) == 2:             # 不跨天情况
        return time_diff
    else:
        if "+1" in table[2]:
            return time_diff + 24*3600  # 跨一天在基础结果上加24小时
        elif "+2" in table[2]:
            return time_diff + 48*3600  # 跨两天在基础结果上加48小时
    # 没考虑如果跨更多天怎么写, 题中说最多飞24小时就这么办吧
        
def main():
    T = int(input())
    for _ in range(T):
        rounds = []
        for i in range(2):
            b = input().splitlines()
            rounds.append(timediff(b))           # 存储单程时间
        answer = (rounds[0] + rounds[1]) // 2    # 航班飞行时间
        print(f"{answer//3600 :02d}:{answer%3600 // 60 :02d}:{answer%60 :02d}")
        # f字符串:02d表示宽度为2左边补0

if __name__ == "__main__":
    main()