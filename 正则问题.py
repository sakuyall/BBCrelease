"""1/1/26
正则问题
    对于正则表达式((xx|xxx)x|(x|xx))xx
    ()表示先后逻辑, x表示某字符串, 只需要管x串长度即可
    |表示或运算, 也就是在前后取最长的x串, 关于右结合律……好像无所谓吧?

字符串最小单元
    遇到()|时跳过, 当这三种符号位于x后出现时输出当前子串长度
    遇到|时准备判断其前后长度, 并输出长的x数量

字符串串联
    将最小单元数值相加, 直到出现)和|

或运算
    分别求取|左右两侧的串联数值, 接着取两者最大值

.rstrip()删除末尾所有不可见字符, 仅删除空格可以用.rstrip(" ")
"""
def parse_factor():
    global pos
    if s[pos] == "x":      # 当前位置为x字符, 指针右移, 返回长度1
        pos += 1
        return 1
    elif s[pos] == "(":
        pos += 1           # 跳过(
        val = parse_expr()
        pos += 1           # 跳过)
        return val

def parse_term():
    global pos
    length = parse_factor()  # 获取初始长度
    while pos < len(s) and s[pos] not in (")", "|"):
        length += parse_factor()
    return length

def parse_expr():
    global pos
    left = parse_term()
    if pos < len(s) and s[pos] == "|":
        pos += 1
        right = parse_expr()      # 调用自身返回单元长度
        return max(left, right)   # 有比较返回大的, 无比较直接返回前边长度
    return left
    
def main():
    global pos, s
    s = str(input()).rstrip()     # 由于本题输入内容结尾有多余空格, 因此需要删除
    pos = 0
    print(parse_expr())

if __name__ == "__main__":
    main()