"""12/31/25
2025图形
    先判断h除以4
    余1按照2025写
    余2按照0252写
    余3按照2520写
    余4按照5202写
    按照此四位数规律写w位

w除以4的商-->完整"2025"个数
余数就在"2025"中切出来相应个数
最后合并字符串
"""
# 考完试复工的第一道题还可以接受
def num_extend(row):
    # 使用字典来映射
    base_map = {1:"2025",
                2:"0252",
                3:"2520",
                0:"5202"
    }
    return base_map[row % 4]

def main():
    h, w = map(int, input().split(" "))
    for row in range(1, h + 1):
        # 为了和实际行数对应，这里从1开始计数
        base = num_extend(row)
        row_answer = base * (w // 4) + base[:w % 4]
        print(row_answer)

if __name__ == "__main__":
    main()