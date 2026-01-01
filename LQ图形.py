"""1/1/26
输出h行长度为w字符串
再输出w行长度为w+v字符串
字符串内容只有Q
"""
def main():
    w, h, v = map(int, input().split(" "))
    # 输出 h 行长度为 w 的 Q 串
    for i in range(h):
        print("Q" * w)
    # 输出 w 行长度为 w+v 的 Q 串
    for j in range(w):
        print("Q" * (w + v))

if __name__ == "__main__":
    main()