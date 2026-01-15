"""1/15/26
ASCII转换函数chr()与ord()
在字母范围内, 把ASCII码加1再对26取余获取下一位置, 而且解决z到a的问题
判断字母大小是否处于字母范围, 如果是其他字符则直接返回本身

注意要用当前字符码减去开头a的码, 使范围缩到a到z
加1后对26取余, 接着加回ord("a")并还原为字符串格式
"""
def encrypt_abc(char):
    if "a" <= char <= "z":
        return chr((ord(char) - ord("a") + 1) % 26 + ord("a"))
    elif "A" <= char <= "Z":
        return chr((ord(char) - ord("A") + 1) % 26 + ord("A"))
    else:
        return char

s = str(input())
li_s = [encrypt_abc(char) for char in s]
print("".join(li_s))